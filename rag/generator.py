# from tts_stt_backend.rag.config import LLM_MODEL

# from tts_stt_backend.rag.llm.phi2 import Phi2LLM

# _llm = None  # private singleton


# def get_llm():
#     global _llm
#     if _llm is None:
#         _llm = Phi2LLM()  # loads once, cached
#     return _llm

from tts_stt_backend.rag.llm.factory import get_llm


def generate_answer(context: str, question: str) -> str:
    
    prompt = f"""

Answer based only on the context below.

Context:
{context}

Question:
{question}

Answer:
"""
    llm = get_llm()
    return llm.generate(prompt)


# def generate_answer(context: str, question: str) -> str:
#     prompt = f"""
# You are a document-based assistant.

# RULES:
# - Answer ONLY using the provided context
# - If the answer is NOT in the context, say:
#   "The answer is not available in the provided documents."
# - Do NOT use external knowledge

# Context:
# {context}

# Question:
# {question}

# Answer:
# """
#     return llm.generate(prompt)
