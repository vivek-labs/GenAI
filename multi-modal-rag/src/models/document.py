from dataclasses import dataclass
from src.models.metadata import DocumentMetadata

@dataclass
class Document:
    document_id: str
    text: str
    metadata: DocumentMetadata
