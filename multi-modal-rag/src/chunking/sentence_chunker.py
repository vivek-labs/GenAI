from __future__ import annotations
import uuid
from src.chunking.base_chunker import BaseChunker
from src.models.chunk import Chunk
from src.models.document import Document
from typing import List 

class SentenceChunker(BaseChunker):
    """
    Sentence-aware chunker.

    Strategy:
    - Split text into sentences
    - Accumulate sentences until chunk_size is reached
    - Neve
    """

    def __init__(self, chunk_size: int = 800):
        self.chunk_size=chunk_size
    
    def chunk(self, document: List[Document]) -> List[Chunk]:
        chunks: List[Chunk] = []
        current_chunk=""
        current_size = 0

        for doc in document:
            #Simple sentence splitting
            #Limitation to fix later: 
            #  1 fails for U.S.A and Mr. Vivek and 3.14 kinda words
            sentences = doc.text.split(". ")

            for sentence in sentences:
                sentence = sentence.strip()
                if not sentence:
                    continue
                #Add a dot (.) back as spplit removed it
                sentence = sentence + ". "
                if current_size + len(sentence) <= self.chunk_size:
                    current_chunk += sentence
                    current_size += len(sentence)
                else:
                    chunks.append(
                        Chunk(
                            chunk_id=str(uuid.uuid4()),
                            document_id=doc.document_id,
                            text=current_chunk.strip(),
                            metadata=doc.metadata
                        )
                    )
                    current_chunk = sentence
                    current_size = len(sentence)
            # save remaining chunk
            if current_chunk.strip():
                chunks.append(
                    Chunk(
                        chunk_id=str(uuid.uuid4()),
                        document_id=doc.document_id,
                        text=current_chunk.strip(),
                        metadata=doc.metadata

                    )
                )
        return chunks
