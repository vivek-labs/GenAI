from pathlib import Path
from src.ingestion.base_extractor import BaseExtractor
from src.ingestion.pdf_extractor import PDFExtractor
from src.ingestion.docx_extractor import DOCXExtractor
class ExtractorFactory:

    @staticmethod
    def create(file_path: str) -> BaseExtractor:
        extension = Path(file_path).suffix.lower()

        if extension == ".pdf":
            return PDFExtractor()
        if extension == ".docx":
            return DOCXExtractor()
        

        raise ValueError(
            f"Unsupported file type: {extension}"
        )