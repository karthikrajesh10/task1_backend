import os
import pickle
import faiss
from tts_stt_backend.rag.embeddings.minilm import MiniLMEmbedding
from tts_stt_backend.rag.utils import chunk_text

INDEX_DIR = "tts_stt_backend/rag/index"
INDEX_PATH = f"{INDEX_DIR}/index.faiss"
META_PATH = f"{INDEX_DIR}/index.pkl"

DOCUMENTS_DIR = "tts_stt_backend/rag/documents"

def load_documents():
    docs = []
    for file in os.listdir(DOCUMENTS_DIR):
        if file.endswith(".txt"):
            with open(os.path.join(DOCUMENTS_DIR, file), "r", encoding="utf-8") as f:
                docs.append(f.read())
    return docs

def build_index():
    os.makedirs(INDEX_DIR, exist_ok=True)

    embedding_model = MiniLMEmbedding()

    docs = load_documents()
    chunks = []

    for doc in docs:
        chunks.extend(chunk_text(doc))

    embeddings = embedding_model.embed(chunks)

    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(embeddings)

    faiss.write_index(index, INDEX_PATH)

    with open(META_PATH, "wb") as f:
        pickle.dump(chunks, f)

    print(f"✅ FAISS index built with {len(chunks)} chunks")

if __name__ == "__main__":
    build_index()
