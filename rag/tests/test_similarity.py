import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from tts_stt_backend.rag.embeddings.minilm import MiniLMEmbedding

embedder = MiniLMEmbedding()

sentences = [
    "Ashok Leyland manufactures trucks",
    "Ashok Leyland produces buses",
    "The ocean is very deep"
]

embeddings = embedder.embed(sentences)
query = embedder.embed_query("What does Ashok Leyland make?")

scores = cosine_similarity(query, embeddings)[0]

for s, score in zip(sentences, scores):
    print(f"{score:.3f} → {s}")
