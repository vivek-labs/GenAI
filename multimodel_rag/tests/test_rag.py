from __future__ import annotations
from src.ingestion.pdf_extractor import PDFExtractor
from src.chunking.simple_chunker import SimpleChunker
from src.rag.rag_pipeline import RAGPipeline


def test_rag_pipeline():

    extractor = PDFExtractor()
    docs = extractor.extract("/Users/vivekpandey/GenAI/multimodel_rag/data/raw/pdf/PA - Consolidated lecture notes.pdf")

    chunker = SimpleChunker()
    chunks = chunker.chunk(docs)

    rag = RAGPipeline()
    rag.index_chunks(chunks)

    results = rag.retrieve("what is this document about?")

    assert results is not None