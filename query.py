import os
from dotenv import load_dotenv

from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.chains import RetrievalQA
from langchain_groq import ChatGroq
load_dotenv()
embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
db = FAISS.load_local(
    "vectorstore/faiss_index",
    embeddings=embedding_model,
    allow_dangerous_deserialization=True
)


# Step 4: Initialize Groq LLM (Mixtral or Mistral)
llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name="mistral-saba-24b",
    temperature=1
      # or "mistral-7b"
)

# Step 5: Create a retrieval-based QA chain
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=db.as_retriever(),
    return_source_documents=False
)

# Step 6: Ask user for a question and print the result
while True:
    query = input("\nAsk a question (or type 'exit' to quit): ")
    if query.lower() in ["exit", "quit"]:
        break
    answer = qa_chain.invoke(query)
    print("\nAnswer:\n", answer)
