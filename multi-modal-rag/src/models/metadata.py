from dataclasses import dataclass
@dataclass
class DocumentMetadata:
    source_file: str
    file_type: str
    page_number: int