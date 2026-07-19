import pytest

from src.ingestion.extractor_factory import ExtractorFactory
from src.ingestion.pdf_extractor import PDFExtractor
from src.ingestion.docx_extractor import DOCXExtractor

def test_create_pdf_extractor():
    extractor = ExtractorFactory.create("notes.pdf")
    assert isinstance(extractor, PDFExtractor)

def test_create_docx_extractor():
    extractor = ExtractorFactory.create("notes.docx")
    assert isinstance(extractor, DOCXExtractor)

def test_create_unsupported_extractor():
    with pytest.raises(ValueError):
        ExtractorFactory.create("notes.ext")
    




