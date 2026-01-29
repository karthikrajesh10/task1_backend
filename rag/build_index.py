# # import os
# # import pickle
# # import faiss
# # from tts_stt_backend.rag.embeddings.minilm import MiniLMEmbedding
# # from tts_stt_backend.rag.utils import chunk_text

# # INDEX_DIR = "tts_stt_backend/rag/index"
# # INDEX_PATH = f"{INDEX_DIR}/index.faiss"
# # META_PATH = f"{INDEX_DIR}/index.pkl"

# # DOCUMENTS_DIR = "tts_stt_backend/rag/documents"

# # def load_documents():
# #     docs = []
# #     for file in os.listdir(DOCUMENTS_DIR):
# #         if file.endswith(".txt"):
# #             with open(os.path.join(DOCUMENTS_DIR, file), "r", encoding="utf-8") as f:
# #                 docs.append(f.read())
# #     return docs

# # def build_index():
# #     os.makedirs(INDEX_DIR, exist_ok=True)

# #     embedding_model = MiniLMEmbedding()

# #     docs = load_documents()
# #     chunks = []

# #     for doc in docs:
# #         chunks.extend(chunk_text(doc))

# #     embeddings = embedding_model.embed(chunks)

# #     dim = embeddings.shape[1]
# #     index = faiss.IndexFlatL2(dim)
# #     index.add(embeddings)

# #     faiss.write_index(index, INDEX_PATH)

# #     with open(META_PATH, "wb") as f:
# #         pickle.dump(chunks, f)

# #     print(f"✅ FAISS index built with {len(chunks)} chunks")

# # if __name__ == "__main__":
# #     build_index()


# # import os
# # import pickle
# # import faiss

# # from tts_stt_backend.rag.embeddings.minilm import MiniLMEmbedding
# # from tts_stt_backend.rag.utils import chunk_text
# # from tts_stt_backend.rag.loaders.pdf_loader import load_pdf

# # INDEX_DIR = "tts_stt_backend/rag/index"
# # INDEX_PATH = f"{INDEX_DIR}/index.faiss"
# # META_PATH = f"{INDEX_DIR}/index.pkl"

# # DOCUMENTS_DIR = "tts_stt_backend/rag/documents"


# # def load_documents():
# #     docs = []

# #     for file in os.listdir(DOCUMENTS_DIR):
# #         path = os.path.join(DOCUMENTS_DIR, file)

# #         if file.endswith(".txt"):
# #             with open(path, "r", encoding="utf-8") as f:
# #                 docs.append(f.read())

# #         elif file.endswith(".pdf"):
# #             docs.append(load_pdf(path))

# #     return docs


# # def build_index():
# #     os.makedirs(INDEX_DIR, exist_ok=True)

# #     embedding_model = MiniLMEmbedding()

# #     documents = load_documents()
# #     chunks = []

# #     for doc in documents:
# #         chunks.extend(chunk_text(doc))

# #     print(f"🔹 Total chunks: {len(chunks)}")

# #     embeddings = embedding_model.embed(chunks)

# #     dim = embeddings.shape[1]
# #     index = faiss.IndexFlatL2(dim)
# #     index.add(embeddings)

# #     faiss.write_index(index, INDEX_PATH)

# #     with open(META_PATH, "wb") as f:
# #         pickle.dump(chunks, f)

# #     print(f"✅ FAISS index built with {len(chunks)} chunks")


# # if __name__ == "__main__":
# #     build_index()


# # import os
# # import pickle
# # import faiss
# # import numpy as np

# # from tts_stt_backend.rag.embeddings.minilm import MiniLMEmbedding
# # from tts_stt_backend.rag.utils import chunk_text

# # from tts_stt_backend.rag.loaders.db_loader import DatabaseLoader
# # from tts_stt_backend.rag.loaders.pdf_loader import PDFLoader
# # from tts_stt_backend.rag.loaders.excel_loader import ExcelLoader
# # from tts_stt_backend.rag.loaders.image_loader import ImageLoader
# # from tts_stt_backend.rag.loaders.txt_loader import TXTLoader


# # # ---------------- PATHS ----------------

# # BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# # DOCUMENTS_DIR = os.path.join(BASE_DIR, "documents")
# # INDEX_DIR = os.path.join(BASE_DIR, "index")

# # INDEX_PATH = os.path.join(INDEX_DIR, "index.faiss")
# # META_PATH = os.path.join(INDEX_DIR, "index.pkl")


# # # ---------------- BUILD INDEX ----------------

# # def build_index():
# #     print("🔄 Building RAG index...")

# #     loaders = []

# #     # Document subfolders
# #     txt_dir = os.path.join(DOCUMENTS_DIR, "txt")
# #     pdf_dir = os.path.join(DOCUMENTS_DIR, "pdf")
# #     excel_dir = os.path.join(DOCUMENTS_DIR, "excel")
# #     image_dir = os.path.join(DOCUMENTS_DIR, "images")

# #     # Register loaders only if folders exist
# #     if os.path.exists(txt_dir):
# #         loaders.append(TXTLoader(txt_dir))

# #     if os.path.exists(pdf_dir):
# #         loaders.append(PDFLoader(pdf_dir))

# #     if os.path.exists(excel_dir):
# #         loaders.append(ExcelLoader(excel_dir))

# #     if os.path.exists(image_dir):
# #         loaders.append(ImageLoader(image_dir))

# #     if not loaders:
# #         raise RuntimeError("❌ No document loaders found. Check documents folder.")

# #     # 1️⃣ Load documents
# #     raw_documents = []
# #     for loader in loaders:
# #         raw_documents.extend(loader.load())

# #     if not raw_documents:
# #         raise RuntimeError("❌ No documents loaded.")

# #     print(f"📄 Loaded {len(raw_documents)} documents")

# #     # 2️⃣ Chunk documents
# #     chunks = []
# #     for doc in raw_documents:
# #         text = doc["text"]
# #         chunks.extend(chunk_text(text))

# #     print(f"✂️ Created {len(chunks)} text chunks")

# #     # 3️⃣ Embed chunks
# #     embedder = MiniLMEmbedding()
# #     embeddings = embedder.embed(chunks).astype("float32")

# #     # 4️⃣ Build FAISS index
# #     dim = embeddings.shape[1]
# #     index = faiss.IndexFlatL2(dim)
# #     index.add(embeddings)

# #     # 5️⃣ Save index + metadata
# #     os.makedirs(INDEX_DIR, exist_ok=True)

# #     faiss.write_index(index, INDEX_PATH)

# #     with open(META_PATH, "wb") as f:
# #         pickle.dump(chunks, f)

# #     print(f"✅ FAISS index built successfully")
# #     print(f"📦 Index path: {INDEX_PATH}")
# #     print(f"📦 Metadata path: {META_PATH}")


# # # ---------------- ENTRYPOINT ----------------

# # if __name__ == "__main__":
# #     build_index()


# import os
# import pickle
# import faiss
# import numpy as np

# from tts_stt_backend.rag.embeddings.minilm import MiniLMEmbedding
# from tts_stt_backend.rag.utils import chunk_text

# from tts_stt_backend.rag.loaders.db_loader import DatabaseLoader
# from tts_stt_backend.rag.loaders.pdf_loader import PDFLoader
# from tts_stt_backend.rag.loaders.excel_loader import ExcelLoader
# from tts_stt_backend.rag.loaders.image_loader import ImageLoader
# from tts_stt_backend.rag.loaders.txt_loader import TXTLoader


# # ---------------- PATHS ----------------

# BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# DOCUMENTS_DIR = os.path.join(BASE_DIR, "documents")
# INDEX_DIR = os.path.join(BASE_DIR, "index")

# INDEX_PATH = os.path.join(INDEX_DIR, "index.faiss")
# META_PATH = os.path.join(INDEX_DIR, "index.pkl")


# # ---------------- BUILD INDEX ----------------

# def build_index():
#     print("🔄 Building RAG index...")

#     loaders = []

#     # Document subfolders
#     txt_dir = os.path.join(DOCUMENTS_DIR, "txt")
#     pdf_dir = os.path.join(DOCUMENTS_DIR, "pdf")
#     excel_dir = os.path.join(DOCUMENTS_DIR, "excel")
#     image_dir = os.path.join(DOCUMENTS_DIR, "images")

#     # Register loaders only if folders exist
#     if os.path.exists(txt_dir):
#         loaders.append(TXTLoader(txt_dir))

#     if os.path.exists(pdf_dir):
#         loaders.append(PDFLoader(pdf_dir))

#     if os.path.exists(excel_dir):
#         loaders.append(ExcelLoader(excel_dir))

#     if os.path.exists(image_dir):
#         loaders.append(ImageLoader(image_dir))

#     if not loaders:
#         raise RuntimeError("❌ No document loaders found. Check rag/documents folder.")

#     # 1️⃣ Load documents
#     raw_documents = []
#     for loader in loaders:
#         loaded = loader.load()
#         if not isinstance(loaded, list):
#             raise TypeError(
#                 f"❌ Loader {loader.__class__.__name__} must return List[dict]"
#             )
#         raw_documents.extend(loaded)

#     if not raw_documents:
#         raise RuntimeError("❌ No documents loaded from loaders.")

#     print(f"📄 Loaded {len(raw_documents)} documents")

#     # 2️⃣ Chunk documents (DEFENSIVE)
#     chunks = []

#     for i, doc in enumerate(raw_documents):
#         # 🔒 Defensive validation
#         if not isinstance(doc, dict):
#             raise TypeError(
#                 f"❌ Document #{i} is not dict → {type(doc)} → {doc}"
#             )

#         if "text" not in doc:
#             raise KeyError(
#                 f"❌ Document #{i} missing 'text' key → {doc}"
#             )

#         text = doc["text"]

#         if not isinstance(text, str):
#             raise TypeError(
#                 f"❌ Document #{i} 'text' is not string → {type(text)}"
#             )

#         if not text.strip():
#             # Skip empty content safely
#             continue

#         doc_chunks = chunk_text(text)

#         if not doc_chunks:
#             continue

#         chunks.extend(doc_chunks)

#     if not chunks:
#         raise RuntimeError("❌ No text chunks created. Check chunking logic.")

#     print(f"✂️ Created {len(chunks)} text chunks")

#     # 3️⃣ Embed chunks
#     embedder = MiniLMEmbedding()
#     embeddings = embedder.embed(chunks)

#     if not isinstance(embeddings, np.ndarray):
#         raise TypeError("❌ Embeddings must be numpy array")

#     embeddings = embeddings.astype("float32")

#     # 4️⃣ Build FAISS index
#     dim = embeddings.shape[1]
#     index = faiss.IndexFlatL2(dim)
#     index.add(embeddings)

#     # 5️⃣ Save index + metadata
#     os.makedirs(INDEX_DIR, exist_ok=True)

#     faiss.write_index(index, INDEX_PATH)

#     with open(META_PATH, "wb") as f:
#         pickle.dump(chunks, f)

#     print("✅ FAISS index built successfully")
#     print(f"📦 Index path: {INDEX_PATH}")
#     print(f"📦 Metadata path: {META_PATH}")


# # ---------------- ENTRYPOINT ----------------

# if __name__ == "__main__":
#     build_index()


import os
import pickle
import faiss
import numpy as np

from tts_stt_backend.rag.embeddings.minilm import MiniLMEmbedding
from tts_stt_backend.rag.utils import chunk_text

from tts_stt_backend.rag.loaders.db_loader import DatabaseLoader
from tts_stt_backend.rag.loaders.mysql_loader import MySQLLoader
from tts_stt_backend.rag.loaders.pdf_loader import PDFLoader
from tts_stt_backend.rag.loaders.excel_loader import ExcelLoader
from tts_stt_backend.rag.loaders.image_loader import ImageLoader
from tts_stt_backend.rag.loaders.txt_loader import TXTLoader


# ---------------- PATHS ----------------

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DOCUMENTS_DIR = os.path.join(BASE_DIR, "documents")
INDEX_DIR = os.path.join(BASE_DIR, "index")

INDEX_PATH = os.path.join(INDEX_DIR, "index.faiss")
META_PATH = os.path.join(INDEX_DIR, "index.pkl")


# ---------------- BUILD INDEX ----------------

def build_index():
    print("🔄 Building RAG index...")

    loaders = []

    # ---------- DOCUMENT LOADERS ----------

    txt_dir = os.path.join(DOCUMENTS_DIR, "txt")
    pdf_dir = os.path.join(DOCUMENTS_DIR, "pdf")
    excel_dir = os.path.join(DOCUMENTS_DIR, "excel")
    image_dir = os.path.join(DOCUMENTS_DIR, "images")

    if os.path.exists(txt_dir):
        loaders.append(TXTLoader(txt_dir))

    if os.path.exists(pdf_dir):
        loaders.append(PDFLoader(pdf_dir))

    if os.path.exists(excel_dir):
        loaders.append(ExcelLoader(excel_dir))

    if os.path.exists(image_dir):
        loaders.append(ImageLoader(image_dir))

    # ---------- SQLITE DATABASE (OPTIONAL) ----------

    # sqlite_db_path = os.path.join(DOCUMENTS_DIR, "db", "employees.db")

    # if os.path.exists(sqlite_db_path):
    #     loaders.append(
    #         DatabaseLoader(
    #             db_path=sqlite_db_path,
    #             query="SELECT * FROM employees"
    #         )
    #     )

    # ---------- MYSQL DATABASE (STUDENTS) ----------

    loaders.append(
        MySQLLoader(
            host="localhost",
            user="root",
            password="karthi710",
            database="rag_demo",
            query="SELECT * FROM students"
        )
    )

    if not loaders:
        raise RuntimeError("❌ No loaders registered. Check configuration.")

    # ---------- LOAD DOCUMENTS ----------

    raw_documents = []

    for loader in loaders:
        loaded = loader.load()

        if not isinstance(loaded, list):
            raise TypeError(
                f"❌ Loader {loader.__class__.__name__} must return List[dict]"
            )

        raw_documents.extend(loaded)

    if not raw_documents:
        raise RuntimeError("❌ No documents loaded from any source.")

    print(f"📄 Loaded {len(raw_documents)} documents")

    # ---------- CHUNK DOCUMENTS ----------

    chunks = []

    for i, doc in enumerate(raw_documents):

        if not isinstance(doc, dict):
            raise TypeError(
                f"❌ Document #{i} is not dict → {type(doc)}"
            )

        if "text" not in doc:
            raise KeyError(
                f"❌ Document #{i} missing 'text' key"
            )

        text = doc["text"]

        if not isinstance(text, str):
            raise TypeError(
                f"❌ Document #{i} 'text' is not string → {type(text)}"
            )

        if not text.strip():
            continue

        doc_chunks = chunk_text(text)

        if doc_chunks:
            chunks.extend(doc_chunks)

    if not chunks:
        raise RuntimeError("❌ No text chunks created.")

    print(f"✂️ Created {len(chunks)} text chunks")

    # ---------- EMBEDDINGS ----------

    embedder = MiniLMEmbedding()
    embeddings = embedder.embed(chunks)

    if not isinstance(embeddings, np.ndarray):
        raise TypeError("❌ Embeddings must be numpy array")

    embeddings = embeddings.astype("float32")

    # ---------- FAISS INDEX ----------

    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(embeddings)

    # ---------- SAVE ----------

    os.makedirs(INDEX_DIR, exist_ok=True)

    faiss.write_index(index, INDEX_PATH)

    with open(META_PATH, "wb") as f:
        pickle.dump(chunks, f)

    print("✅ FAISS index built successfully")
    print(f"📦 Index path: {INDEX_PATH}")
    print(f"📦 Metadata path: {META_PATH}")


# ---------------- ENTRYPOINT ----------------

if __name__ == "__main__":
    build_index()
