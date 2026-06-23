from typing import List

from src.embeddings.openai_embeddings import OpenAIEmbedding
from src.vectorstore.chroma_store import ChromaStore
from src.models.chunk import Chunk


class RAGPipeline:

    def __init__(self):

        self.embedder = OpenAIEmbedding()
        self.vectorstore = ChromaStore()

    def index_chunks(self, chunks: List[Chunk]):

        texts = [c.text for c in chunks]
        embeddings = self.embedder.embed(texts)

        self.vectorstore.add_chunks(chunks, embeddings)

    def retrieve(self, query: str):

        query_embedding = self.embedder.embed([query])[0]

        results = self.vectorstore.search(query_embedding)

        return results