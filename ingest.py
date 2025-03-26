import os
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from dotenv import load_dotenv
load_dotenv()
document = "C:\\Users\\happi\\OneDrive\\Desktop\\RAGAI\\PDF\\Designing Data-Intensive Applications The Big Ideas Behind Reliable, Scalable, and Maintainable Systems ( PDFDrive ).pdf"
loader=PyPDFLoader(document)
documents=loader.load()
splitter=RecursiveCharacterTextSplitter(chunk_size=500,chunk_overlap=100)
docs=splitter.split_documents(documents)
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
db = FAISS.from_documents(docs, embeddings)
db.save_local("vectorstore/faiss_index")
print(f"Ingested {len(docs)} chunks from sample.pdf")

