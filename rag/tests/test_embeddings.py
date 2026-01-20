from tts_stt_backend.rag.embeddings.minilm import MiniLMEmbedding

embedder = MiniLMEmbedding()

texts = [
    "Ashok Leyland manufactures trucks",
    "The sky is blue",
    "Buses are produced by Ashok Leyland"
]

embeddings = embedder.embed(texts)

print("Embedding shape:", embeddings.shape)
