from src.ingestion.pdf_extractor import PDFExtractor

def test_pdf_extraction_basic():

    extractor = PDFExtractor()

    docs = extractor.extract("/Users/vivekpandey/GenAI/multimodel_rag/data/raw/pdf/PA - Consolidated lecture notes.pdf")

    # should return something
    assert isinstance(docs, list)

    # if PDF is valid, should have at least 1 page
    assert len(docs) > 0

    # check structure
    assert hasattr(docs[0], "text")
    assert hasattr(docs[0], "metadata")