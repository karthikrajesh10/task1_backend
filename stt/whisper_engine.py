import whisper
from stt.base import BaseSTT

class WhisperSTTEngine(BaseSTT):
    def __init__(self, model_size="base"):
        self.model = whisper.load_model(model_size)

    def transcribe(self, audio_file: str, language: str | None = None) -> str:
        if language:
            result = self.model.transcribe(audio_file, language=language)
        else:
            #auto detect
            result = self.model.transcribe(audio_file)

        return result["text"]
