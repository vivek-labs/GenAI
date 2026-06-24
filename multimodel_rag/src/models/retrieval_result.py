from dataclasses import dataclass
from src.models.metadata import DocumentMetadata
@dataclass
class RetrievalResult:
    text: str
    metadata: DocumentMetadata
    distance: float