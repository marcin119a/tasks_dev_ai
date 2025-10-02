# Adresowo RAG App

Retrieval-Augmented Generation (RAG) app built with **LangChain**, **Chroma**, and **Gradio**, using real estate data from Adresowo. The app allows users to semantically search property descriptions using sentence embeddings and view the top-matching offers.

---

## Features

- Parses and stores Polish real estate descriptions.
- Chunks text and builds a vector database (Chroma) using HuggingFace embeddings.
- Enables semantic search through a user-friendly Gradio interface.
- Runs fully containerized with Docker Compose.

---

## Requirements

- Docker
- Docker Compose

---

## 📁 Project structure

```
.
├── .env # Environment variables (output folder, port)
├── app.py # Gradio app interface
├── build_files.py # Downloads and stores property descriptions as .txt files
├── build_vectorstore.py # Builds vector DB from description chunks
├── start.sh # Launches build + app
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── README.md
```

## Configuration

Edit the `.env` file to customize folder and port:

```env
OUTPUT_FOLDER=adresowo_descriptions
PORT=7860
```

### Build and run the app
# Step 1: Build and launch the container
```
docker-compose up --build
```

Visit:
```
http://localhost:7860
```

### Recommended: Detached mode (run in background)
```
docker-compose up -d --build
```

### Access container shell
```
docker exec -it rag-rag-app-1 /bin/bash
```