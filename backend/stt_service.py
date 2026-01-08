from tts_stt_backend.config.settings import STT_ENGINE


def speech_to_text(audio_file: str, language: str | None = None) -> str:
    return STT_ENGINE.transcribe(audio_file, language)
