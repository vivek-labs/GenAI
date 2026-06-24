from typing import List

from src.embeddings.openai_embeddings import OpenAIEmbedding
from src.models.retrieval_result import RetrievalResult
from src.models.metadata import DocumentMetadata
from src.vectorstore.chroma_store import ChromaStore
from src.models.chunk import Chunk
from src.llm.openai_llm import OpenAILLM
from src.prompt.prompt_builder import PromptBuilder


class RAGPipeline:

    def __init__(self):

        self.embedder = OpenAIEmbedding()
        self.vectorstore = ChromaStore()
        self.llm = OpenAILLM()

    def index_chunks(self, chunks: List[Chunk]):

        texts = [chunk.text for chunk in chunks]
        embeddings = self.embedder.embed(texts)

        self.vectorstore.add_chunks(chunks, embeddings)

    def retrieve(self, query: str):

        query_embedding = self.embedder.embed([query])[0]
        raw_results = self.vectorstore.search(query_embedding)
        retrieval_results=[]
        documents=raw_results["documents"][0]
        metadatas=raw_results["metadatas"][0]
        distances=raw_results["distances"][0]

        for text,metadata,distance in zip(documents,metadatas,distances):
            doc_metadata = DocumentMetadata(
                source_file=metadata["source"],
                file_type=metadata["file_type"],
                page_number=metadata["page"]

            )

            retrieval_results.append(
                RetrievalResult(
                    text=text,
                    metadata=doc_metadata,
                    distance=distance
                )
            )

        return retrieval_results
    def ask(self,query:str) -> str:
        results = self.retrieve(query)
        context = "\n\n".join(result.text for result in results)
        prompt = PromptBuilder.build_rag_prompt(
            query=query,
            context=context
        )
        answer = self.llm.generate(prompt)
        return answer