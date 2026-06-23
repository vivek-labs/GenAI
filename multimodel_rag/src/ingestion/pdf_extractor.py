from __future__ import annotations
import fitz #PyMuPDF
from typing import List
from src.models.document import Document
from src.models.metadata import DocumentMetadata


class PDFExtractor:
    """
    Extracts text from PDF and converts into structured Document objects.
    - One document = one page
    - No logger for now : To Do
    - No external utilities : Will do later
    """

    def __init__(self):
        pass

    def extract(self, file_path:str) -> List[Document]:
        #logger.info(f"Starting PDF extraction: {file_path}")
        doc = fitz.open(file_path)
        documents: List[Document] = []

        for page_number in range(len(doc)):
            page = doc.load_page(page_number)
            text = page.get_text("text")

            #Basic cleanup, will improve later
            cleaned_text = self._clean_text(text)
            #Skip empty pages
            if not cleaned_text.strip():
                continue
            
            metadata = DocumentMetadata(
                source_file = file_path.split("/")[-1],
                file_type = "pdf",
                page_number=page_number + 1
            )

            document = Document(
                document_id=str(page_number), #Simple MVP Id
                text = cleaned_text,
                metadata=metadata
            )

            documents.append(document)
        return documents
    
    def _clean_text(self,text:str) -> str:
        """"
        Minimal cleaning only:
        - remove newlines
        - normalize spaces
        """
        text = text.replace("\n", " ")
        text = " ".join(text.split())
        return text
