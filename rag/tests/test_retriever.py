# from tts_stt_backend.rag.retriever import retrieve_context

# query = "What vehicles does Ashok Leyland manufacture?"

# context = retrieve_context(query)

# print("Retrieved context:\n")
# print(context)


# from tts_stt_backend.rag.retriever import retrieve_context

# query = "What is Article 21?"

# context = retrieve_context(query)

# print("Retrieved context:\n")
# print(context)


from tts_stt_backend.rag.retriever import retrieve_context

queries = [
    "What is Article 21 of the Constitution of India?",
    "What vehicles does Ashok Leyland manufacture?",
    "Who is the CEO of Google?",
    "Give examples of female employees from Pune",
    "The quick brown dog jumped over what?",
    "Give examples of students from computer science department"

    
]

for q in queries:
    print("\nQUESTION:", q)
    context = retrieve_context(q)
    print("CONTEXT FOUND:\n", context if context else "[NO CONTEXT]")

