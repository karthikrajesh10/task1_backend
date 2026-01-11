from abc import ABC, abstractmethod

class BaseTTS(ABC):
    @abstractmethod
    def synthesize(self, text: str, output_path: str) -> None:
        pass
