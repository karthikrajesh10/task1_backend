from tts_stt_backend.rag.retriever import retrieve_context
from tts_stt_backend.rag.generator import generate_answer

question = "What is Ashok Leyland known for?"

context = retrieve_context(question)
answer = generate_answer(context, question)

print("Context:\n", context)
print("\nAnswer:\n", answer)
