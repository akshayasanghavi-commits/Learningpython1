README.md
📚 Agentic RAG System with Local LLM (Fully Offline)

This project implements a multi-source Retrieval-Augmented Generation (RAG) system capable of answering questions from PDF documents, structured databases, and live web search.

The system uses a multi-agent architecture where a routing agent determines the most relevant data source, retrieves context, and generates answers using a local LLM.

An end-to-end Agentic Retrieval-Augmented Generation (RAG) system built using:

Custom document ingestion pipeline

Semantic search with FAISS

Local LLM (FLAN-T5)

Multi-agent orchestration using CrewAI

Designed for extensibility (memory, SQL tools, web search, UI)

This project demonstrates real-world AI system architecture beyond simple tutorials.

🚀 Project Overview

This system enables users to:

Upload and process PDF documents

Convert document text into semantic embeddings

Store vectors in FAISS vector database

Retrieve relevant document chunks using similarity search

Generate context-aware answers using a local LLM

Orchestrate intelligent workflows using multi-agent architecture

The entire system runs locally — no paid APIs required.

🧠 Architecture
User Query
   ↓
Router Agent
   ↓
PDF Retriever | SQL Tool | Web Tool
   ↓
Answer Agent
   ↓
Final Response

🏗 Core Components
1️⃣ Document Ingestion

PDF loading

Text extraction

Recursive chunking

2️⃣ Embeddings & Vector Store

Sentence embeddings via SentenceTransformers

Vector storage using FAISS

Semantic similarity search

3️⃣ Local LLM

Model: ollama

Runs fully offline after first download

No API keys required

No usage cost

4️⃣ Agentic Layer

Multi-agent orchestration using CrewAI:

Retrieval Agent (uses custom vector tool)

Answer Agent (generates contextual responses)

Future: Critique & Reflection Agent

📂 Project Structure
rag_doc_qa/
│
├── ingestion/
│   ├── pdf_loader.py
│   └── text_chunker.py
│
├── embeddings/
│   └── embedder.py
│
├── retrieval/
│   ├── search.py
│   └── rag_pipeline.py
│
├── agents/
│   ├── tools.py
│   └── crew_setup.py
│
├── vector_store/
│   ├── faiss_index.index
│   └── chunks.pkl
│
├── data/
│   └── raw_pdfs/
│
└── README.md

🔧 Setup Instructions
1️⃣ Create Virtual Environment
python -m venv rag_venv


Activate:

.\rag_venv\Scripts\Activate

2️⃣ Install Dependencies
pip install pandas numpy
pip install sentence-transformers
pip install faiss-cpu
pip install transformers torch
pip install crewai langchain langchain-community
pip install streamlit

3️⃣ Run Pipeline
Step A – Create Embeddings
python embeddings\embedder.py

Step B – Run Agentic System
python agents\crew_setup.py

🎯 Why This Project Matters

This project demonstrates:

✔ Custom RAG implementation
✔ Vector database understanding
✔ Embedding generation
✔ Agent-based AI orchestration
✔ conversatiom memory
✔ SQL Tool
✔ Web Search Tool
✔  Streamlit Chat
✔ Local LLM integration
✔ Modular architecture

This is closer to real production AI systems than simple API-based chatbots.



🧑‍💻 Learning Outcomes

Through building this system, you gain understanding of:

Transformer-based LLMs

Semantic embeddings

Vector similarity search

Retrieval-Augmented Generation (RAG)

Agent-based AI workflows

Local model deployment

🏆 Ideal For

AI/ML Engineer portfolio

LLM system design practice

RAG experimentation

Agentic AI exploration

Interview discussion on AI architecture

🔥 Author Goal

This project is designed as a continuously evolving AI system — not a one-time tutorial build.

The objective is to grow it into a production-style multi-agent AI assistant.
