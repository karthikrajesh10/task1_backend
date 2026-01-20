from sentence_transformers import SentenceTransformer
from tts_stt_backend.rag.embeddings.base import BaseEmbedding

class MiniLMEmbedding(BaseEmbedding):

    def __init__(self):
        self.model = SentenceTransformer("all-MiniLM-L6-v2")

    def embed(self, texts):
        return self.model.encode(texts)

    def embed_query(self, query):
        return self.model.encode([query])
