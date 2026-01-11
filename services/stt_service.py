from tts_stt_backend.config.settings import STT_ENGINE
from tts_stt_backend.services.translation import translate_to_english

def speech_to_text(audio_path: str, language: str | None) -> tuple[str, str]:
    original_text = STT_ENGINE.transcribe(audio_path, language)

    if language and language.lower() not in ["en", "en-us", "en-in"]:
        english_text = translate_to_english(original_text)
    else:
        english_text = original_text

    return original_text, english_text
