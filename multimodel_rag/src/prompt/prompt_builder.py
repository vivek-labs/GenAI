class PromptBuilder:
    @staticmethod
    def build_rag_prompt(query:str, context:str) ->str:
        return f"""
                you are a helpful assistant.
                Anser ONLY from the provided context.
                Context:{context} 
                Question:{query}
                """
    
