# # from fastapi import FastAPI
# # from fastapi.staticfiles import StaticFiles
# # from tts_stt_backend.api.auth import router as auth_router
# # from tts_stt_backend.api.chat import router as chat_router


# # app = FastAPI(title="Voice Assistant Backend")

# # app.mount("/audio", StaticFiles(directory="output/audio"), name="audio")

# # app.include_router(auth_router)
# # app.include_router(chat_router)


# from fastapi import FastAPI
# from fastapi.staticfiles import StaticFiles
# from pathlib import Path
# from tts_stt_backend.api.auth import router as auth_router
# from tts_stt_backend.api.chat import router as chat_router

# app = FastAPI(title="Voice Assistant Backend")

# BASE_DIR = Path(__file__).resolve().parent.parent
# AUDIO_DIR = BASE_DIR / "output" / "audio"

# app.mount("/audio", StaticFiles(directory=AUDIO_DIR), name="audio")

# app.include_router(auth_router)
# app.include_router(chat_router)


from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from tts_stt_backend.api.auth import router as auth_router
from tts_stt_backend.api.chat import router as chat_router
from tts_stt_backend.config.settings import AUDIO_DIR

app = FastAPI(title="Voice Assistant Backend")

# 🔥 SAME directory used by TTS
app.mount(
    "/audio",
    StaticFiles(directory=str(AUDIO_DIR)),
    name="audio"
)

app.include_router(auth_router)
app.include_router(chat_router)
