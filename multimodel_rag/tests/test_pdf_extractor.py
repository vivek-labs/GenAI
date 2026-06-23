from src.ingestion.pdf_extractor import PDFExtractor

def test_pdf_extraction_basic(sample_pdf_path):

    extractor = PDFExtractor()

    docs = extractor.extract(str(sample_pdf_path))

    # should return something
    assert isinstance(docs, list)

    # if PDF is valid, should have at least 1 page
    assert len(docs) > 0

    # check structure
    assert hasattr(docs[0], "text")
    assert hasattr(docs[0], "metadata")