import chromadb
from typing import List
from src.models.chunk import Chunk
from src.vectorstore.base_vectorstore import BaseVectorStore

class ChromaStore(BaseVectorStore):
    def __init__(self, collection_name: str = "rag_name"):
        self.client = chromadb.PersistentClient(path="data/chroma")
        self.collection = self.client.get_or_create_collection(
            name=collection_name
        )
    
    def add_chunks(self, chunks: List[Chunk], embeddings: List[List[float]]):
        self.collection.add(
            ids=[chunk.chunk_id for chunk in chunks],
            embeddings=embeddings,
            documents=[chunk.text for chunk in chunks],
            metadatas=[
                {
                    "document_id": chunk.document_id,
                    "page": chunk.metadata.page_number,
                    "source": chunk.metadata.source_file,
                    "file_type": chunk.metadata.file_type
                }
                for chunk in chunks
            ]
        )
    def search(self, query_embedding: List[float], top_k: int=5):
        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k
        )
        return results