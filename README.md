<h1>WikiTalks</h1>
<h4>An AI powered roleplaying Wikipedia assistant using Retrieval-Augmented Generation (RAG).</h4>
<hr>
<br>
<p><b>WikiTalks</b> is a <i>Retrieval-Augmented Generation (RAG)</i> application that brings Wikipedia pages to life. It helps user to <i>interact with Wikipedia pages through Natural Language Conversations</i>.</p>
<h5>How This Application Works :</h5>
<ol>
    <li>The application retrieves information from the desired <i>Wikipedia page.</i></li>
    <li>Converts the content into <i>Semantic Chunks.</i></li>
    <li>Store them in a <i>Vector Database</i> (Here, <i>ChromaDB</i> was used).</li>
    <li>Then with help of a <i>Large Language Model (LLM)</i> it generates relevant responses.</li>
</ol>

<h5>Features :</h5>

<ul>
    <li>Wikipedia Article Scrapping</li>
    <li>Semantic Chunking</li>
    <li>Vector Embedding</li>
    <li>ChromaDB Vector Storage</li>
    <li>Uses Gemma 4 31B as LLM</li>
    <li>Context Aware Question Answering</li>
    <li>Character Style Responses</li>
    <li>Streamlit Web Interface</li>
</ul>

<h5>Tech Stack :</h5>

<ul>
    <li>Python</li>
    <li>Streamlit</li>
    <li>Wikipedia API</li>
    <li>Sentence Transformers</li>
    <li>Chroma DB</li>
    <li>Semchunk</li>
    <li>Cerebras API</li>
    <li>Gemma 4 31B</li>
</ul>

<hr>
<h3>Installation :</h3>
<hr>
<h5>Cloning repository and Downloading Required Packages :</h5>

<code>git clone https://github.com/SujonG1/WikiTalks</code>
<br>
<code>cd WikiTalks</code>
<br>
<code>pip install -r requirements.txt</code>

<hr>
<h5>Create Environment Variable :</h5>
<p>You will need to get your own free API key from https://www.cerebras.ai/</p>

<br>
<p>Create a .env file and store your API key there</p>

<code>CEREBRAS_API_KEY="your_api_key_here"</code>

<hr>
<h5>Run :</h5>

<code>streamlit run app.py</code>

<hr>
<h1>Thank You for Reading!</h1>