from src.ingestion.pdf_extractor import PDFExtractor
from src.chunking.simple_chunker import SimpleChunker


def test_chunking():

    extractor = PDFExtractor()
    docs = extractor.extract("/Users/vivekpandey/GenAI/multimodel_rag/data/raw/pdf/PA - Consolidated lecture notes.pdf")

    chunker = SimpleChunker(chunk_size=500, overlap=50)
    chunks = chunker.chunk(docs)

    assert len(chunks) > 0
    assert hasattr(chunks[0], "text")
    assert len(chunks[0].text) > 0