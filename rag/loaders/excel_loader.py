# # import pandas as pd
# # from pathlib import Path
# # from tts_stt_backend.rag.loaders.base import BaseLoader

# # class ExcelLoader(BaseLoader):
# #     def __init__(self, directory: str):
# #         self.directory = Path(directory)

# #     def load(self):
# #         texts = []
# #         for file in self.directory.glob("*.xlsx"):
# #             df = pd.read_excel(file)
# #             texts.append(df.to_string(index=False))
# #         return texts


# import pandas as pd
# from pathlib import Path
# from tts_stt_backend.rag.loaders.base import BaseLoader


# class ExcelLoader(BaseLoader):
#     def __init__(self, directory: str):
#         self.directory = Path(directory)

#         if not self.directory.exists():
#             raise FileNotFoundError(f"Excel/CSV directory not found: {directory}")

#     def load(self) -> list[str]:
#         texts = []

#         # Load Excel files
#         for file in self.directory.glob("*.xlsx"):
#             df = pd.read_excel(file)
#             texts.append(df.to_string(index=False))

#         # Load CSV files
#         for file in self.directory.glob("*.csv"):
#             df = pd.read_csv(file)
#             texts.append(df.to_string(index=False))

#         return texts


import pandas as pd
from pathlib import Path
from tts_stt_backend.rag.loaders.base import BaseLoader


# class ExcelLoader(BaseLoader):
#     def __init__(self, directory: str):
#         self.directory = Path(directory)

#     def load(self):
#         documents = []

#         for file in self.directory.glob("*.xlsx"):
#             df = pd.read_excel(file)
#             documents.append({
#                 "text": df.to_string(index=False),
#                 "source": file.name,
#                 "type": "excel"
#             })

#         for file in self.directory.glob("*.csv"):
#             df = pd.read_csv(file)
#             documents.append({
#                 "text": df.to_string(index=False),
#                 "source": file.name,
#                 "type": "csv"
#             })

#         return documents


class ExcelLoader(BaseLoader):
    def __init__(self, directory: str):
        self.directory = Path(directory)

    def load(self):
        documents = []

        for file in self.directory.glob("*.xlsx"):
            df = pd.read_excel(file)
            documents.append({
                "text": df.to_string(index=False),
                "source": file.name,
                "type": "excel"
            })

        for file in self.directory.glob("*.csv"):
            df = pd.read_csv(file)
            documents.append({
                "text": df.to_string(index=False),
                "source": file.name,
                "type": "csv"
            })

        return documents
