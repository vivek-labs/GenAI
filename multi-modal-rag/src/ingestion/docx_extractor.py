
from docx import Document as DocxDocument
from docx.opc.exceptions import PackageNotFoundError
from typing import List
from pathlib import Path

from src.models.document import Document
from src.models.metadata import DocumentMetadata
from src.ingestion.base_extractor import BaseExtractor

class DOCXExtractor(BaseExtractor):

    def extract(self, file_path: str) -> List[Document]:
        path = Path(file_path)

        if path.suffix.lower() != ".docx":
            raise ValueError(f"Expected a .docx file, received: {path.suffix}")

        if not path.exists():
            raise FileNotFoundError(f"File not found: {file_path}")
        
        try:
            docx_file = DocxDocument(file_path)
        except PackageNotFoundError as exception:
            raise ValueError(
                f"Invalid or corrupted DOCX file: {file_path}"
            ) from exception
        
        paragraphs = [
            paragraph.text.strip() for paragraph in docx_file.paragraphs
            if paragraph.text.strip()
        ]

        text = "\n".join(paragraphs)

        if not text:
            return []
        
        metadata = DocumentMetadata(
            source_file = str(path),
            page_number = 1,
            file_type = "docx"
        )

        return [
            Document (
                document_id = path.stem,
                text = text,
                metadata=metadata
            )
        ]
