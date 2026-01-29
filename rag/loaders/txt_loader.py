# from pathlib import Path
# from tts_stt_backend.rag.loaders.base import BaseLoader


# class TXTLoader(BaseLoader):
#     def __init__(self, directory: str):
#         self.directory = Path(directory)

#         if not self.directory.exists():
#             raise FileNotFoundError(f"TXT directory not found: {directory}")

#     def load(self) -> list[str]:
#         texts = []

#         for file in self.directory.glob("*.txt"):
#             with open(file, "r", encoding="utf-8") as f:
#                 content = f.read().strip()

#                 if content:
#                     texts.append(content)
#                 else:
#                     print(f"⚠️ Empty TXT skipped: {file.name}")

#         return texts


import os
from tts_stt_backend.rag.loaders.base import BaseLoader


class TXTLoader(BaseLoader):
    def __init__(self, directory: str):
        self.directory = directory

    def load(self):
        documents = []

        for filename in os.listdir(self.directory):
            if filename.endswith(".txt"):
                path = os.path.join(self.directory, filename)

                with open(path, "r", encoding="utf-8") as f:
                    text = f.read()

                documents.append({
                    "text": text,
                    "source": filename,
                    "type": "txt"
                })

        return documents
