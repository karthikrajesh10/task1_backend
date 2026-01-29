# # from pypdf import PdfReader

# # def load_pdf(path: str) -> str:
# #     reader = PdfReader(path)
# #     pages = []

# #     for page in reader.pages:
# #         text = page.extract_text()
# #         if text:
# #             pages.append(text)

# #     return "\n".join(pages)


# from pathlib import Path
# from pypdf import PdfReader
# from tts_stt_backend.rag.loaders.base import BaseLoader


# class PDFLoader(BaseLoader):

#     def __init__(self, directory: str):
#         self.directory = Path(directory)

#         if not self.directory.exists():
#             raise FileNotFoundError(f"PDF directory not found: {directory}")

#     def load(self) -> list[str]:
#         documents = []

#         for pdf_path in self.directory.glob("*.pdf"):
#             reader = PdfReader(pdf_path)
#             pages = []

#             for page in reader.pages:
#                 text = page.extract_text()
#                 if text:
#                     pages.append(text)

#             full_text = "\n".join(pages)

#             if full_text.strip():
#                 documents.append(full_text)
#             else:
#                 print(f"⚠️ Empty PDF skipped: {pdf_path.name}")

#         return documents


from pathlib import Path
from pypdf import PdfReader
from tts_stt_backend.rag.loaders.base import BaseLoader


class PDFLoader(BaseLoader):
    def __init__(self, directory: str):
        self.directory = Path(directory)

    def load(self):
        documents = []

        for file in self.directory.glob("*.pdf"):
            reader = PdfReader(file)
            pages = []

            for page in reader.pages:
                text = page.extract_text()
                if text:
                    pages.append(text)

            documents.append({
                "text": "\n".join(pages),
                "source": file.name,
                "type": "pdf"
            })

        return documents
