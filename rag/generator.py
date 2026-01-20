from tts_stt_backend.rag.config import LLM_MODEL

def generate_answer(context: str, question: str) -> str:
    prompt = f"""
Answer based only on the context below.

Context:
{context}

Question:
{question}

Answer:
"""
    return LLM_MODEL.generate(prompt)
