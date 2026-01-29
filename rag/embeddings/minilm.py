# from sentence_transformers import SentenceTransformer
# from tts_stt_backend.rag.embeddings.base import BaseEmbedding

# class MiniLMEmbedding(BaseEmbedding):

#     def __init__(self):
#         self.model = SentenceTransformer("all-MiniLM-L6-v2")

#     def embed(self, texts):
#         return self.model.encode(texts)

#     def embed_query(self, query):
#         return self.model.encode([query])

from sentence_transformers import SentenceTransformer
import numpy as np
from tts_stt_backend.rag.embeddings.base import BaseEmbedding
from pathlib import Path

class MiniLMEmbedding(BaseEmbedding):

    def __init__(self):
        model_path = Path("tts_stt_backend/models/minilm")

        if not model_path.exists():
            raise RuntimeError(
                "MiniLM model not found locally. "
                "Please download and save it to tts_stt_backend/models/minilm"
            )

        self.model = SentenceTransformer(
            str(model_path),
            device="cpu"   # safe for backend servers
        )

    def embed(self, texts: list[str]) -> np.ndarray:
        return self.model.encode(
            texts,
            convert_to_numpy=True,
            normalize_embeddings=True
        )

    def embed_query(self, query: str) -> np.ndarray:
        return self.model.encode(
            [query],
            convert_to_numpy=True,
            normalize_embeddings=True
        )
