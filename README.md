🗣️ Voice Assistant Backend (TTS + STT + RAG)

This backend powers a chatbot-style voice assistant that supports:

-   User Authentication (Signup & Login)
-   Text-to-Speech (TTS)
-   Speech-to-Text (STT) with multi-language support
-   Retrieval-Augmented Generation (RAG) from local documents (offline)
-   REST APIs exposed via FastAPI
-   Interactive API testing using Swagger UI

------------------------------------------------------------------------

ARCHITECTURE OVERVIEW

Frontend (Streamlit) | | HTTP (JSON / Multipart) v FastAPI Backend ├──
Auth (JWT) ├── Chat API │ ├── STT (voice → text) │ ├── RAG (retrieve +
generate) │ └── TTS (text → audio) ├── FAISS Vector DB (offline) └──
Local LLM + Embeddings

------------------------------------------------------------------------

MAIN API ROUTES

1)  Signup POST /auth/signup

Request: { “username”: “user1”, “password”: “password123” }

Response: { “message”: “User created successfully” }

------------------------------------------------------------------------

2)  Login POST /auth/login

Request: { “username”: “user1”, “password”: “password123” }

Response: { “access_token”: “eyJhbGciOiJIUzI1NiIs…”, “token_type”:
“bearer” }

This token must be sent in the Authorization header for protected APIs.

------------------------------------------------------------------------

3)  Chat (Text or Voice) POST /chat

Headers: Authorization: Bearer

Text Input (Form-data): text = “What is the Trademark Act?” language =
“en”

Voice Input (Form-data): audio = voice.wav language = “ml” / “hi” / “en”

Response: { “type”: “voice”, “original_text”: “example”, “english_text”:
“example”, “audio”: “/audio/abc123.mp3” }

------------------------------------------------------------------------

SWAGGER API DOCUMENTATION

Open in browser after starting server: http://127.0.0.1:8000/docs

You can test APIs, upload audio, and pass JWT tokens directly.

------------------------------------------------------------------------

RAG (Retrieval-Augmented Generation)

Supported document sources: - .txt - .pdf - .xlsx, .csv - Images (OCR) -
SQLite databases

RAG Flow: 1. Load documents 2. Chunk text 3. Create embeddings using
MiniLM 4. Store in FAISS 5. Retrieve relevant chunks and generate
answers using LLM

No internet knowledge is used at inference time.

------------------------------------------------------------------------

SPEECH MODULES

Speech-to-Text (STT): - Google Speech Recognition - Multi-language
support - Voice to English text

Text-to-Speech (TTS): - Microsoft Edge Neural Voices - Text to audio
output - Served via /audio route

------------------------------------------------------------------------

BACKEND SETUP

1)  Clone repository git clone cd tts_stt_backend

2)  Create virtual environment python -m venv venv venv

3)  Install dependencies pip install -r requirements.txt

4)  Build RAG index python -m tts_stt_backend.rag.build_index

5)  Start server uvicorn tts_stt_backend.api.main:app –reload

------------------------------------------------------------------------

AUDIO OUTPUT LOCATION

tts_stt_backend/output/audio/

Access: http://127.0.0.1:8000/audio/.mp3

------------------------------------------------------------------------

SECURITY NOTES

-   Passwords hashed with bcrypt
-   JWT required for protected routes
-   RAG uses only local data

------------------------------------------------------------------------

SUMMARY

-   FastAPI backend
-   JWT authentication
-   Text and Voice chat
-   Offline RAG
-   Swagger testing
-   Modular architecture
