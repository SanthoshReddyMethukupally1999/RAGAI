import os
import streamlit as st
from dotenv import load_dotenv
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.chains import RetrievalQA
from langchain_groq import ChatGroq

# Load environment variables
load_dotenv()

# Set Streamlit page
st.set_page_config(page_title="RAGAI Assistant", layout="centered")
st.title("📄 RAGAI — Ask your PDF")

# Load FAISS vector store
embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
db = FAISS.load_local("vectorstore/faiss_index", embedding_model, allow_dangerous_deserialization=True)

# Load Groq LLM
llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name="mistral-saba-24b"  
)

# Set up RetrievalQA chain
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=db.as_retriever(),
    return_source_documents=True
)

# UI Input
user_query = st.text_input("Ask a question about your document:")
on=st.toggle("Source Chunks")
if on:
    qa_chain.return_source_documents=True
else:
    qa_chain.return_source_documents=False
# Button to get the answer
if st.button("Get Answer"):
    if user_query.strip():
        response = qa_chain.invoke(user_query)
        st.subheader("Answer:")
        st.write(response["result"])

        # Show sources
        if qa_chain.return_source_documents==True:
            st.subheader("Source Chunks:")
            for i, doc in enumerate(response["source_documents"]):
                st.markdown(f"**Chunk {i+1}:**")
                st.info(doc.page_content)
    else:
        st.warning("Please enter a valid question.")