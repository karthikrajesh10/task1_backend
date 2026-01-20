from tts_stt_backend.rag.generator import generate_answer

context = """
Ashok Leyland is an Indian automotive company.
It manufactures trucks, buses, and defense vehicles.
"""

question = "What does Ashok Leyland manufacture?"

answer = generate_answer(context, question)

print(answer)
