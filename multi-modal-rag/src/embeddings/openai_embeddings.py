from typing import List
from openai import OpenAI
from src.embeddings.base_embedding import BaseEmbedding

class OpenAIEmbedding(BaseEmbedding):
    def __init__(self, model: str = "text-embedding-3-small"):
        self.client = OpenAI()
        self.model = model
    
    def embed(self, texts: List[str]) -> List[List[float]]:
        response = self.client.embeddings.create(
            model=self.model,
            input=texts
        )
        return [item.embedding for item in response.data]