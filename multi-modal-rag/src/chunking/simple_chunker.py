from __future__ import annotations
from typing import List
import uuid

from src.models.document import Document
from src.models.chunk import Chunk
from src.chunking.base_chunker import BaseChunker


class SimpleChunker(BaseChunker):
    """
    Minimal chunker for Phase 1 RAG.

    Strategy:
    - character-based splitting
    - fixed overlap
    """

    def __init__(self, chunk_size: int = 800, overlap: int = 100):
        if overlap >= chunk_size:
            raise ValueError(
            "overlap must be smaller than chunk_size"
        )
        self.chunk_size = chunk_size
        self.overlap = overlap

    def chunk(self, documents: List[Document]) -> List[Chunk]:

        chunks: List[Chunk] = []

        for doc in documents:

            text = doc.text

            start = 0

            while start < len(text):

                end = start + self.chunk_size
                chunk_text = text[start:end]

                if not chunk_text.strip():
                    break

                new_chunk = Chunk(
                    chunk_id=str(uuid.uuid4()),
                    document_id=doc.document_id,
                    text=chunk_text,
                    metadata=doc.metadata
                )

                chunks.append(new_chunk)
                start += self.chunk_size - self.overlap

        return chunks