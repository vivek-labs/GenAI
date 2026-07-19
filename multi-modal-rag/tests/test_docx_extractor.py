from src.ingestion.docx_extractor import DOCXExtractor
import pytest

def test_docx_extraction_basic(sample_basic_docx_path):

    extractor = DOCXExtractor()
    docs = extractor.extract(str(sample_basic_docx_path))

    # should return something
    assert isinstance(docs, list)

    # if DOCX is valid, should have at least 1 page
    assert len(docs) > 0

    # check structure
    assert hasattr(docs[0], "text")
    assert hasattr(docs[0], "metadata")

def test_docx_extraction_missing_file():
    extractor = DOCXExtractor()
    with pytest.raises(FileNotFoundError):
        extractor.extract("filenotfound.docx")

def test_docx_extraction_invalid_extension(tmp_path):
    extractor = DOCXExtractor()
    fake_file = tmp_path / "notes.ext"
    fake_file.write_text("dummy")

    with pytest.raises(ValueError):
        extractor.extract(str(fake_file))

    #test absent file
    with pytest.raises(FileNotFoundError):
        doc = extractor.extract("filenotfound.docx")
    
    #ValueError
    with pytest.raises(ValueError):
        doc = extractor.extract("filenotfound.ext")

def test_docx_extraction_emptyfile(sample_empty_docx_path):
    extractor = DOCXExtractor()
    docs = extractor.extract(str(sample_empty_docx_path))
    assert len(docs) == 0



    
