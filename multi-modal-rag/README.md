# Multi-Modal RAG

Multi-Modal RAG is a lightweight retrieval-augmented generation project for extracting text from PDFs, chunking it, embedding the chunks, storing them in Chroma, and answering questions with an OpenAI model.

## What it does

- Extracts text from PDF files with PyMuPDF.
- Splits documents into overlapping chunks.
- Generates embeddings with OpenAI.
- Stores and searches vectors with ChromaDB.
- Builds grounded answers with source citations.

## Project layout

- `src/ingestion` - PDF extraction.
- `src/chunking` - text chunking.
- `src/embeddings` - embedding interfaces and OpenAI implementation.
- `src/vectorstore` - vector store interfaces and Chroma implementation.
- `src/llm` - LLM interfaces and OpenAI implementation.
- `src/rag` - the main RAG pipeline.
- `tests` - automated tests for extraction, chunking, and retrieval.

## Requirements

- Python 3.9+
- An OpenAI API key in the environment as `OPENAI_API_KEY`

## Install

From the repository root:

```bash
pip install -r requirements.txt
```

## Run tests

From `multi-modal-rag`:

```bash
python -m pytest -v tests
```

## Release notes

## v0.3.0

### Added
- BaseExtractor abstraction
- ExtractorFactory
- DOCX document ingestion
- Multi-format ingestion architecture

### Changed
- PDFExtractor now implements BaseExtractor
