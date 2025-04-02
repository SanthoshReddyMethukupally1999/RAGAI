"# RAGAI" 
Load the PDF using PyPDFLoader
The PyPDFLoader reads the document and extracts its contents into a structured format, typically page by page.
At this stage, the document is effectively added to your knowledge base in text form.

Chunk the content using RecursiveCharacterTextSplitter
The full text is split into smaller overlapping chunks (for example, 500 characters with 100-character overlap).
This ensures that each chunk is within the context window of an LLM and helps preserve important context across boundaries.

Generate embeddings using Hugging Face
Each text chunk is transformed into a vector using a sentence-transformer model, such as all-MiniLM-L6-v2.
These embeddings numerically represent the semantic meaning of each chunk, allowing for similarity search.

Store the embeddings in a FAISS vector database
The generated vectors are stored locally in a FAISS index.
This index enables fast retrieval of the most relevant chunks when a user submits a query later.

# RAGAI — Retrieval-Augmented Generation PDF Assistant

RAGAI is a Retrieval-Augmented Generation (RAG) system that allows users to interact with the content of a PDF using a Large Language Model (LLM). It retrieves relevant information from a document and augments the query to produce more accurate and context-aware responses.

---

## 🚀 Features

- Upload and process any PDF using LangChain's PyPDFLoader  
- Chunk documents using RecursiveCharacterTextSplitter  
- Generate embeddings using HuggingFace (MiniLM)  
- Store vectors in a local FAISS database  
- Ask questions and receive responses powered by Groq + Mistral  
- Simple and interactive UI built with Streamlit  
- Optional toggle to show source chunks used in responses

---

## 🧠 How It Works

### Ingest (`ingest.py`)
1. Loads PDF content using `PyPDFLoader`
2. Splits the content into overlapping chunks
3. Generates vector embeddings using HuggingFace (`all-MiniLM-L6-v2`)
4. Stores vectors in a FAISS vector database locally

### Query (`query.py` or `app.py`)
1. Accepts a user question
2. Embeds the query and retrieves similar chunks from FAISS
3. Sends the retrieved context + query to an LLM (Mistral via Groq)
4. Displays the generated answer (and optionally shows sources)

---

## 🛠️ Tech Stack

- Python 3.10+  
- LangChain  
- HuggingFace Embeddings  
- FAISS  
- Groq (Mistral-24B)  
- Streamlit  
- dotenv

---

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Santhoshreddy1999/RAGAI.git
cd RAGAI

2.Create Virtual Environment

python -m venv ven
# Activate it:
# On Windows:
ven\Scripts\activate
# On Mac/Linux:
source ven/bin/activate

3. Install Requirements

pip install -r requirements.txt

4. Set Up Environment Variables
Create a .env file in the project root and add your Groq API key:
GROQ_API_KEY=your_groq_api_key_here

5. Embed the PDF
Place your PDF in a folder (e.g., PDF/) and edit the path in ingest.py, then run:

python ingest.py

6. Launch the UI

streamlit run app.py
