from __future__ import annotations
from src.ingestion.pdf_extractor import PDFExtractor
from src.models.metadata import DocumentMetadata
from src.models.document import Document

def main():
    extractor = PDFExtractor()
    docs = extractor.extract("/Users/vivekpandey/GenAI/multimodel_rag/data/raw/pdf/PA - Consolidated lecture notes.pdf")
    print("Total pages extracted:", len(docs))

    if docs:
        print("\n--- SAMPPLE PAGE ---")
        print(docs[0].text[:500])
        print(docs[0].metadata)
    
if __name__ == "__main__":
    main()