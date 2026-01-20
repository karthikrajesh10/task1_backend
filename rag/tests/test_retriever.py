from tts_stt_backend.rag.retriever import retrieve_context

query = "What vehicles does Ashok Leyland manufacture?"

context = retrieve_context(query)

print("Retrieved context:\n")
print(context)
