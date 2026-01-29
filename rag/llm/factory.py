from tts_stt_backend.rag.llm.distilgpt2 import DistilGPT2LLM

_LLM_INSTANCE = None

def get_llm():
    global _LLM_INSTANCE
    if _LLM_INSTANCE is None:
        _LLM_INSTANCE = DistilGPT2LLM()  # ✅ INSTANCE
    return _LLM_INSTANCE
