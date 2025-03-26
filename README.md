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

