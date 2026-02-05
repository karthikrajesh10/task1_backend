🗣️ Voice Assistant Backend (TTS + STT + RAG)

This backend powers a chatbot-style voice assistant that supports:

✅ User authentication (Signup & Login)

✅ Text-to-Speech (TTS)

✅ Speech-to-Text (STT) with multi-language support

✅ Retrieval-Augmented Generation (RAG) from local documents (offline)

✅ REST APIs exposed via FastAPI

✅ Interactive API testing using Swagger UI

🏗️ Architecture Overview
Frontend (Streamlit)
        |
        |  HTTP (JSON / Multipart)
        v
FastAPI Backend
 ├── Auth (JWT)
 ├── Chat API
 │    ├── STT (voice → text)
 │    ├── RAG (retrieve + generate)
 │    └── TTS (text → audio)
 ├── FAISS Vector DB (offline)
 └── Local LLM + Embeddings

🔑 Main API Routes

The backend exposes 3 primary routes:

1️⃣ Signup

POST /auth/signup

Creates a new user account.

Request (JSON):

{
  "username": "user1",
  "password": "password123"
}


Response:

{
  "message": "User created successfully"
}

2️⃣ Login

POST /auth/login

Authenticates the user and returns a JWT access token.

Request (JSON):

{
  "username": "user1",
  "password": "password123"
}


Response:

{
  "access_token": "eyJhbGciOiJIUzI1NiIs...",
  "token_type": "bearer"
}


This token must be sent in the Authorization header for all protected APIs.

3️⃣ Chat (Text or Voice)

POST /chat

This is the core endpoint.

It supports:

📝 Text input → RAG → Answer → Audio

🎙️ Voice input → STT → RAG → Answer → Audio

Headers:

Authorization: Bearer <access_token>

Text input
Form-data:
text = "What is the Trademark Act?"
language = "en"

Voice input
Form-data:
audio = voice.wav
language = "ml" / "hi" / "en"


Response:

{
  "type": "voice",
  "original_text": "എന്റെ പേര് കാർത്തിക",
  "english_text": "My name is Karthik",
  "audio": "/audio/abc123.mp3"
}

📚 Swagger API Documentation

This backend uses Swagger (OpenAPI) for API documentation and testing.

After starting the server, open:

👉 http://127.0.0.1:8000/docs

Swagger allows you to:

View all available APIs

Send requests without Postman

Upload audio files

Pass JWT tokens

Inspect responses visually

Swagger UI replaces the need for Postman in this project.

🧠 RAG (Retrieval-Augmented Generation)

The chatbot answers questions using only local documents.

Supported document sources:

📄 .txt

📕 .pdf

📊 .xlsx, .csv

🖼️ Images (OCR)

🗄️ Databases (SQLite)

RAG Flow:

Documents are loaded

Text is chunked

Chunks are embedded (MiniLM)

Stored in FAISS

On query → retrieve top chunks → generate answer using LLM

⚠️ No internet knowledge is used at inference time.

🔊 Speech Modules
Speech-to-Text (STT)

Uses Google Speech Recognition

Supports multiple languages

Converts voice → English text

Text-to-Speech (TTS)

Uses Microsoft Edge Neural Voices

Converts generated answers → audio

Audio is served via /audio/* static route

⚙️ Backend Setup Instructions
1️⃣ Clone repository
git clone <repo-url>
cd tts_stt_backend

2️⃣ Create virtual environment
python -m venv venv
venv\Scripts\activate   # Windows

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Build RAG index (one-time)
python -m tts_stt_backend.rag.build_index

5️⃣ Start backend server
uvicorn tts_stt_backend.api.main:app --reload

📦 Audio Output

Generated audio files are stored and served from:

tts_stt_backend/output/audio/


Accessible via:

http://127.0.0.1:8000/audio/<filename>.mp3

🔒 Security Notes

Passwords are hashed using bcrypt

JWT tokens are required for protected routes

No external APIs are called for RAG answers

✅ Summary

✔ FastAPI backend

✔ JWT-based auth

✔ Text + Voice chat

✔ Offline RAG

✔ Swagger-based testing

✔ Modular & extensible design
