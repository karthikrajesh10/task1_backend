from abc import ABC, abstractmethod

class BaseSTT(ABC):
    @abstractmethod
    def transcribe(self, audio_file: str, language: str | None = None) -> str:
        pass
