from __future__ import annotations

import uuid
from typing import List

from src.chunking.base_chunker import BaseChunker
from src.models.chunk import Chunk
from src.models.document import Document


class SentenceChunker(BaseChunker):
    """
    Sentence-aware chunker with optional sentence overlap.
    """

    def __init__(self, chunk_size: int = 800, overlap_sentences: int = 2):
        if chunk_size <= 0:
            raise ValueError("chunk_size must be positive")

        if overlap_sentences < 0:
            raise ValueError("overlap_sentences cannot be negative")

        self.chunk_size = chunk_size
        self.overlap_sentences = overlap_sentences

    def chunk(self, documents: List[Document]) -> List[Chunk]:
        chunks: List[Chunk] = []

        for doc in documents:
            sentences = self._split_sentences(doc.text)

            current_sentences: List[str] = []
            current_size = 0

            for sentence in sentences:
                sentence_size = len(sentence)

                if current_size + sentence_size <= self.chunk_size:
                    current_sentences.append(sentence)
                    current_size += sentence_size
                else:
                    if current_sentences:
                        chunks.append(
                            self._create_chunk(
                                doc=doc,
                                sentences=current_sentences,
                            )
                        )

                    if self.overlap_sentences > 0:
                        overlap = current_sentences[-self.overlap_sentences:]
                    else:
                        overlap = []

                    current_sentences = overlap + [sentence]
                    current_size = sum(len(s) for s in current_sentences)

            if current_sentences:
                chunks.append(
                    self._create_chunk(
                        doc=doc,
                        sentences=current_sentences,
                    )
                )

        return chunks

    def _split_sentences(self, text: str) -> List[str]:
        return [
            sentence.strip() + "."
            for sentence in text.split(". ")
            if sentence.strip()
        ]

    def _create_chunk(
        self,
        doc: Document,
        sentences: List[str],
    ) -> Chunk:
        return Chunk(
            chunk_id=str(uuid.uuid4()),
            document_id=doc.document_id,
            text=" ".join(sentences),
            metadata=doc.metadata,
        )