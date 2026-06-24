from src.ingestion.pdf_extractor import PDFExtractor
from src.chunking.simple_chunker import SimpleChunker


def test_chunking(sample_pdf_path):

    extractor = PDFExtractor()
    docs = extractor.extract(str(sample_pdf_path))

    chunker = SimpleChunker(chunk_size=500, overlap=50)
    chunks = chunker.chunk(docs)

    assert len(chunks) > 0
    assert hasattr(chunks[0], "text")
    assert len(chunks[0].text) > 0