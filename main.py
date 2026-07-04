import streamlit as st
import os
from dotenv import load_dotenv
import wikipediaapi
import semchunk
import chromadb
from sentence_transformers import SentenceTransformer
from transformers import AutoTokenizer
from langchain_cerebras import ChatCerebras

load_dotenv()

st.title("WikiTalk")
st.subheader("Talk to your Wikipedia search.")

api_key = os.getenv("CEREBRAS_API_KEY")
 
llm = ChatCerebras(
    model="gemma-4-31b", 
    api_key=api_key, 
    temperature=0.5
)
 
if "collection" not in st.session_state:
    
    st.session_state.model = SentenceTransformer("all-MiniLM-L6-v2")
    st.session_state.client = chromadb.Client()
    st.session_state.collection = st.session_state.client.get_or_create_collection("wiki_data")
 
query1 = st.text_input("Enter a name:")

if st.button("Load Entity"):
    
    wiki = wikipediaapi.Wikipedia(user_agent='WikiNowApp (sujonganguly01@gmail.com)', language='en')
    page = wiki.page(query1)
    
    if page.exists():

        st.session_state.client.delete_collection("wiki_data")
        st.session_state.collection = st.session_state.client.get_or_create_collection("wiki_data")

        tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
        chunker = semchunk.chunkerify(tokenizer, 250)
        chunks = chunker(
            page.text, 
            overlap=0.1
        )
        
        embedding = st.session_state.model.encode(chunks).tolist()
        st.session_state.collection.add(
            documents = chunks, 
            embeddings = embedding, 
            ids =[f"id_{i}" for i in range(len(chunks))]
        )
        st.success(f"Successfully loaded with {len(chunks)} chunks!")
        
    else:
        
        st.error("Error! 404 Entity not found.")
 
question = st.text_input("Enter your query:")

if st.button("Ask"):
    
    if st.session_state.collection.count() > 0:
        
        query_emb = st.session_state.model.encode(question).tolist()
        results = st.session_state.collection.query(
            query_embeddings = [query_emb], 
            n_results = 5
        )
        
        if results['documents'] and results['documents'][0]:
            
            context = "\n\n".join(results['documents'][0])
            prompt = f"Use this context to answer: {context}, and become the query yourself, you can add some missing information yourself from trusted sources. Avoid breaking character and avoid using phrases that would make you sound like an AI. Be the character and be believable. You may use their quotes in relevant times and try to imitate them\n\nQuestion: {question}"
            answer = llm.invoke(prompt)
            st.subheader(f"Answer from {query1}")
            st.write(answer.content)
            
        else:
            
            st.warning("I don't really remember that.")
            
    else:
        
        st.warning("Load a page first.")