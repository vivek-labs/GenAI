from __future__ import annotations
from src.ingestion.pdf_extractor import PDFExtractor
from src.chunking.simple_chunker import SimpleChunker


def test_rag_pipeline(sample_pdf_path, mock_rag_pipeline):

    extractor = PDFExtractor()
    docs = extractor.extract(str(sample_pdf_path))

    chunker = SimpleChunker()
    chunks = chunker.chunk(docs)

    mock_rag_pipeline.index_chunks(chunks)

    results = mock_rag_pipeline.retrieve("what is this document about?")

    assert results is not None