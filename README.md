# Cocktail Recommendation System

This project is a **Cocktail Recommendation System** that suggests cocktails based on user input. It uses **FAISS** for fast nearest neighbor search and **SentenceTransformers** to encode the cocktail descriptions into vector embeddings.

## Features
- **Cocktail Search**: Enter your desired cocktail wish, and the system will suggest top 3 cocktails matching your input.
- **Fast Search**: Utilizes FAISS for efficient similarity search.
- **Pre-trained Models**: SentenceTransformer is used to encode cocktail names and descriptions.

## Technologies Used
- **FastAPI**: For creating the REST API.
- **Dash**: For building the interactive web interface.
- **FAISS**: For nearest neighbor search.
- **SentenceTransformers**: For encoding and semantic search.
- **Python**: Programming language for the entire project.
- **Dash Bootstrap Components**: For styling the front-end with Bootstrap.

## Model Used: `sentence-transformers/multi-qa-mpnet-base-dot-v1`

The **`multi-qa-mpnet-base-dot-v1`** model is a pre-trained Sentence Transformer model fine-tuned on **multiple-question answering (QA)** tasks. It is capable of encoding text into high-quality vector embeddings, which are ideal for measuring the semantic similarity between queries and documents. In this project, the model is used to encode cocktail names and descriptions into vectors, enabling efficient retrieval and comparison using **FAISS** (Facebook AI Similarity Search).

### Features of the Model:
- **Pre-trained**: The model is pre-trained on large-scale QA datasets and can be directly used for a variety of tasks, including semantic textual similarity, clustering, and search.
- **Text Embedding**: Converts input text (e.g., cocktail descriptions) into fixed-size vectors, allowing for easy comparison and search in vector spaces.
- **Fine-tuned**: The model has been fine-tuned specifically for multiple-question answering tasks, which helps in understanding the context of the input text and finding the most relevant results.