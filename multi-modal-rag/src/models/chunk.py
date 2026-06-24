from dataclasses import dataclass
from src.models.metadata import DocumentMetadata
@dataclass
class Chunk:
    chunk_id: str
    document_id: str
    text: str
    metadata: DocumentMetadata
