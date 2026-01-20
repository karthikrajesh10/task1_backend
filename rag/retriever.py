# import faiss
# import pickle
# import numpy as np
# from tts_stt_backend.rag.config import EMBEDDING_MODEL

# INDEX_PATH = "tts_stt_backend/rag/index/index.faiss"
# META_PATH = "tts_stt_backend/rag/index/index.pkl"

# # Load index & chunks ONCE
# index = faiss.read_index(INDEX_PATH)

# with open(META_PATH, "rb") as f:
#     chunks = pickle.load(f)

# def retrieve_context(query: str, k: int = 3) -> str:
#     # Embed query
#     q_emb = EMBEDDING_MODEL.embed_query(query)

#     # FAISS requires 2D array
#     q_emb = np.array([q_emb])

#     # Search
#     distances, indices = index.search(q_emb, k)

#     # Fetch chunks
#     return "\n".join(chunks[i] for i in indices[0])

import faiss
import pickle
import numpy as np
from tts_stt_backend.rag.config import EMBEDDING_MODEL

INDEX_PATH = "tts_stt_backend/rag/index/index.faiss"
META_PATH = "tts_stt_backend/rag/index/index.pkl"

# Load index and chunks once
index = faiss.read_index(INDEX_PATH)

with open(META_PATH, "rb") as f:
    chunks = pickle.load(f)

def retrieve_context(query: str, k: int = 3) -> str:
    # Get embedding
    q_emb = EMBEDDING_MODEL.embed_query(query)

    #  Ensure shape = (1, dim)
    q_emb = np.asarray(q_emb, dtype="float32")

    if q_emb.ndim == 1:
        q_emb = q_emb.reshape(1, -1)
    elif q_emb.ndim == 2 and q_emb.shape[0] != 1:
        q_emb = q_emb[:1]

    distances, indices = index.search(q_emb, k)

    return "\n".join(chunks[i] for i in indices[0])
