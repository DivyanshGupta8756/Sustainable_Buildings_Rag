# RAG-based LLM System for Sustainable Building Codes

This project implements a Retrieval-Augmented Generation (RAG) system
for querying Indian and global green building standards such as LEED,
GRIHA, IGBC, ECBC, and NBC.

## Features
- Clause-level retrieval from standards
- Semantic search using embeddings
- LLM-based explanation with citations
- Modular, extensible architecture

## Tech Stack
- Python
- LangChain
- Sentence Transformers
- FAISS Vector DB
- OpenAI GPT Models

## Architecture
1. Document ingestion & chunking
2. Embedding generation
3. Vector similarity search
4. LLM-based answer generation

## Setup
```bash
pip install -r requirements.txt
