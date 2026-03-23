class HybridLLM:
    def __init__(self):
        self.api_llm = ChatOpenAI('gpt-4o')  # Gemini/OpenAI API
        self.local_llm = Ollama(model='llama3')  # Offline

    async def invoke(self, prompt):
        try:
            return self.api_llm.invoke(prompt)  # Online priority
        except:
            return self.local_llm.invoke(prompt)  # Offline fallback

# Integrate graphs
llm = HybridLLM()

# Real-time WS update agent status
print("Hybrid LLM Army Connected")

