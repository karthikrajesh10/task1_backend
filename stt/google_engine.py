import speech_recognition as sr
from tts_stt_backend.stt.base import BaseSTT

class GoogleSTTEngine(BaseSTT):

    def transcribe(self, audio_file: str, language: str | None = None) -> str:
        recognizer = sr.Recognizer()

        with sr.AudioFile(audio_file) as source:
            audio = recognizer.record(source)

        return recognizer.recognize_google(audio, language=language)
