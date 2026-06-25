from typing import List

from src.models.retrieval_result import RetrievalResult
from src.models.metadata import DocumentMetadata
from src.models.chunk import Chunk
## No need after dependency injection of base embeddings, bas vectorstore and base llm
#from src.vectorstore.chroma_store import ChromaStore
#from src.embeddings.openai_embeddings import OpenAIEmbedding
#from src.llm.openai_llm import OpenAILLM
from src.prompt.prompt_builder import PromptBuilder
from src.embeddings.base_embedding import BaseEmbedding
from src.vectorstore.base_vectorstore import BaseVectorStore
from src.llm.base_llm import BaseLLM

class RAGPipeline:

    def __init__(self, embedder:BaseEmbedding, vectorstore:BaseVectorStore, llm: BaseLLM):

        self.embedder = embedder
        self.vectorstore = vectorstore
        self.llm = llm

    def index_chunks(self, chunks: List[Chunk]):

        texts = [chunk.text for chunk in chunks]
        embeddings = self.embedder.embed(texts)

        self.vectorstore.add_chunks(chunks, embeddings)

    def retrieve(self, query: str, top_k:int=5, max_distance: float = 0.90):

        query_embedding = self.embedder.embed([query])[0]
        raw_results = self.vectorstore.search(query_embedding,top_k=top_k)
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
            retrieval_results = [
                result for result in retrieval_results
                if result.distance <= max_distance
            ]

        for result in retrieval_results:
            print(result.distance)
        for result in retrieval_results:
            print("\n----------------")
            print(result.metadata.page_number)
            print(result.text[:300])

        return retrieval_results
    

    def _build_context(self,results:List[RetrievalResult]) -> str:
        context = "\n\n".join(result.text for result in results)
        return context

        
    def ask(self,query:str, top_k:int=5, max_distance:float=0.90) -> str:
        results = self.retrieve(query=query,top_k=top_k,max_distance=max_distance)
        if not results:
            return "I could not find relevant information in the provided documents."
        context = self._build_context(results)
        prompt = PromptBuilder.build_rag_prompt(
            query=query,
            context=context
        )
 
        answer = self.llm.generate(prompt)

        #Add sources of answer
        sources=[]
        for result in results:
            source = (
                f"{result.metadata.source_file} "
                f"(Page {result.metadata.page_number})"
            )
            if source not in sources:
                sources.append(source)

        sources_text = "\n".join(f"- {source}" for source in sources)
        return (f"{answer}\n\n"
                f"Sources:\n"
                f"{sources_text}"
        )