import os
from tts_stt_backend.config.settings import TTS_ENGINE


OUTPUT_DIR = "output/audio"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def text_to_speech(text: str, filename: str) -> str:
    """
    Converts text to speech.
    Returns path to generated audio file.
    """
    extension = ".mp3" if TTS_ENGINE.__class__.__name__ == "EdgeTTSEngine" else ".wav"
    audio_path = os.path.join(OUTPUT_DIR, filename + extension)

    TTS_ENGINE.speak(text, audio_path)
    return audio_path
