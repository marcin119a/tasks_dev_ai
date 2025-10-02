import os
import pandas as pd
from dotenv import load_dotenv
from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

# 1. Load environment variables
load_dotenv()
output_folder = os.getenv("OUTPUT_FOLDER", "adresowo_descriptions")

# 2. Load text documents from folder
docs = []
for file in os.listdir(output_folder):
    if file.endswith(".txt"):
        loader = TextLoader(os.path.join(output_folder, file))
        docs.extend(loader.load())

print(f"Loaded {len(docs)} documents from '{output_folder}'")

# 3. Split documents into chunks
chunk_size = int(os.getenv("CHUNK_SIZE", 500))  # Default to 500 if not set
splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=50)
chunks = splitter.split_documents(docs)

print(f"Split into {len(chunks)} chunks.")

# 4. Generate embeddings and build vector DB
embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vectordb = Chroma.from_documents(chunks, embedding, persist_directory="./chroma_index")

print("Vectorstore built and saved in './chroma_index'")