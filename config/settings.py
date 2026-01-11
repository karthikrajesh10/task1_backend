# from tts.edge_tts_engine import EdgeTTSEngine
# from stt.google_engine import GoogleSTTEngine

# # from tts.pyttsx3_engine import Pyttsx3Engine

# # from stt.whisper_engine import WhisperSTTEngine


# # -------- TTS --------
# TTS_ENGINE = EdgeTTSEngine()
# # TTS_ENGINE = Pyttsx3Engine()

# # -------- STT --------
# # STT_ENGINE = WhisperSTTEngine()
# STT_ENGINE = GoogleSTTEngine()

# AUDIO_OUTPUT_DIR = "output/audio"


from tts_stt_backend.stt.google_engine import GoogleSTTEngine

from tts_stt_backend.tts.edge_tts_engine import EdgeTTSEngine

from pathlib import Path

# Project root (TextToSpeech/)
BASE_DIR = Path(__file__).resolve().parents[2]

# Audio output directory
AUDIO_DIR = BASE_DIR / "output" / "audio"

# Ensure directory exists
AUDIO_DIR.mkdir(parents=True, exist_ok=True)


STT_ENGINE = GoogleSTTEngine()
TTS_ENGINE = EdgeTTSEngine()



JWT_SECRET = "CHANGE_ME_SECRET"
JWT_ALGORITHM = "HS256"
JWT_EXPIRE_MINUTES = 60

