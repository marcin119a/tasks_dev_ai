#!/bin/bash

echo "Running build_files.py to prepare text files..."
python3 build_files.py

# Check if vectorstore already exists
if [ ! -d "./chroma_index" ]; then
    echo "Building vectorstore (chroma_index does not exist)..."
    python3 build_vectorstore.py
else
    echo "Vectorstore already exists at './chroma_index'. Skipping build."
fi

echo "Launching Gradio app..."
python3 app.py