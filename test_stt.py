from tts_stt_backend.services.stt_service import speech_to_text

def test_malayalam_stt():
    audio_path = "tts_stt_backend/audio_test/sample_ml.wav"
    language = "ml"  

    original, english = speech_to_text(audio_path, language)

    print("Original Malayalam Text:", original)
    print("Translated English Text:", english)


if __name__ == "__main__":
    test_malayalam_stt()
