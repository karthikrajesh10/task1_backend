from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from tts_stt_backend.api.auth import router as auth_router
from tts_stt_backend.api.chat import router as chat_router


app = FastAPI(title="Voice Assistant Backend")

app.mount("/audio", StaticFiles(directory="output/audio"), name="audio")

app.include_router(auth_router)
app.include_router(chat_router)
