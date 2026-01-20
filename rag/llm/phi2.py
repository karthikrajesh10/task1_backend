from transformers import pipeline
from tts_stt_backend.rag.llm.base import BaseLLM

class Phi2LLM(BaseLLM):

    def __init__(self):
        self.pipe = pipeline(
            "text-generation",
            model="microsoft/phi-2",
            max_new_tokens=200
        )

    def generate(self, prompt: str) -> str:
        result = self.pipe(prompt)[0]["generated_text"]
        return result.split("Answer:")[-1].strip()
