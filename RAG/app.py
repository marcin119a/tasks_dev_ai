from dotenv import load_dotenv
import gradio as gr
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

# 1. Load environment variables
load_dotenv()
embedding_model_name = "sentence-transformers/all-MiniLM-L6-v2"
chroma_path = "./chroma_index"

# 2. Load the embedding model and vector database
embedding = HuggingFaceEmbeddings(model_name=embedding_model_name)
vectordb = Chroma(persist_directory=chroma_path, embedding_function=embedding)

# 3. Define Gradio interface function
def search_offers(query):
    results = vectordb.similarity_search(query, k=3)
    return "\n---\n".join([r.page_content for r in results])

# 4. Launch Gradio UI
iface = gr.Interface(
    fn=search_offers,
    inputs=gr.Textbox(label="Twoje zapytanie"),
    outputs=gr.Textbox(label="Najlepsze dopasowania"),
    title="Wyszukiwarka ofert Adresowo (RAG)"
)

iface.launch(server_name="0.0.0.0", server_port=7860)