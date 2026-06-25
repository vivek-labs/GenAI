from abc import ABC, abstractmethod
from typing import List
from src.chunking.simple_chunker import Chunk

class BaseVectorStore(ABC):
    @abstractmethod
    def add_chunks(self, chunks: List[Chunk], embeddings: List[List[float]]):
        pass

    @abstractmethod
    def search(self, query_embedding: List[float], top_k: int = 5):
        pass    