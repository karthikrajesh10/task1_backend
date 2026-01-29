# from tts_stt_backend.rag.generator import generate_answer

# context = """
# Ashok Leyland is an Indian automotive company.
# It manufactures trucks, buses, and defense vehicles.
# """

# question = "What does Ashok Leyland manufacture?"

# answer = generate_answer(context, question)

# print(answer)

from tts_stt_backend.rag.generator import generate_answer

context = """
Article 21 of the Constitution of India states that no person shall be deprived
of his life or personal liberty except according to procedure established by law.
"""

question = "What does Article 21 guarantee?"

answer = generate_answer(context, question)
print(answer)

