# # import pytesseract
# # from PIL import Image
# # from pathlib import Path
# # from tts_stt_backend.rag.loaders.base import BaseLoader

# # class ImageLoader(BaseLoader):
# #     def __init__(self, directory: str):
# #         self.directory = Path(directory)

# #     def load(self):
# #         texts = []
# #         for img in self.directory.glob("*.*"):
# #             text = pytesseract.image_to_string(Image.open(img))
# #             texts.append(text)
# #         return texts

# from pathlib import Path
# from tts_stt_backend.rag.loaders.base import BaseLoader
# from pytesseract import image_to_string
# from PIL import Image


# class ImageLoader(BaseLoader):
#     def __init__(self, directory: str):
#         self.directory = Path(directory)

#     def load(self):
#         documents = []

#         for file in self.directory.glob("*"):
#             try:
#                 text = image_to_string(Image.open(file))
#                 documents.append({
#                     "text": text,
#                     "source": file.name,
#                     "type": "image"
#                 })
#             except Exception:
#                 continue

#         return documents


from pathlib import Path
from PIL import Image
import pytesseract
from tts_stt_backend.rag.loaders.base import BaseLoader


# 🔒 Always hardcode tesseract path on Windows
pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)


class ImageLoader(BaseLoader):
    def __init__(self, directory: str):
        self.directory = Path(directory)

        if not self.directory.exists():
            raise FileNotFoundError(f"Image directory not found: {directory}")

    def load(self):
        documents = []

        for file in self.directory.glob("*"):
            if file.suffix.lower() not in {".png", ".jpg", ".jpeg", ".tiff"}:
                continue

            try:
                img = Image.open(file)
                text = pytesseract.image_to_string(img)

                text = text.strip()

                if not text:
                    print(f"⚠️ Empty OCR text skipped: {file.name}")
                    continue

                documents.append({
                    "text": text,
                    "source": file.name,
                    "type": "image"
                })

                print(f" OCR extracted from: {file.name}")

            except Exception as e:
                print(f" OCR failed for {file.name}: {e}")

        return documents
