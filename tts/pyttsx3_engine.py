import pyttsx3
from tts.base import BaseTTS

class Pyttsx3Engine(BaseTTS):
    def speak(self, text: str, output_file: str):
        engine = pyttsx3.init()
        engine.save_to_file(text, output_file)
        engine.runAndWait()
