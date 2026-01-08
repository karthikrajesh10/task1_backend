from tts_stt_backend.tts.edge_tts_engine import EdgeTTSEngine
# from tts.pyttsx3_engine import Pyttsx3Engine

# from stt.whisper_engine import WhisperSTTEngine
from tts_stt_backend.stt.google_engine import GoogleSTTEngine

# -------- TTS --------
TTS_ENGINE = EdgeTTSEngine()
# TTS_ENGINE = Pyttsx3Engine()

# -------- STT --------
# STT_ENGINE = WhisperSTTEngine()
STT_ENGINE = GoogleSTTEngine()
