class PromptBuilder:
    @staticmethod
    def build_rag_prompt(query:str, context:str) ->str:
        return f"""
You are a helpful assistant.

Use ONLY the information provided in the context below.

If the answer cannot be found in the context, say:
"I could not find the answer in the provided documents."

Context:
{context}

Question:
{query}

Answer:
"""
    
