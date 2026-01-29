# import sqlite3
# from tts_stt_backend.rag.loaders.base import BaseLoader

# class DatabaseLoader(BaseLoader):
#     def __init__(self, db_path: str, query: str):
#         self.db_path = db_path
#         self.query = query

#     def load(self):
#         conn = sqlite3.connect(self.db_path)
#         cursor = conn.cursor()
#         cursor.execute(self.query)
#         rows = cursor.fetchall()
#         conn.close()

#         return [" | ".join(map(str, row)) for row in rows]


import sqlite3
from tts_stt_backend.rag.loaders.base import BaseLoader


class DatabaseLoader(BaseLoader):
    def __init__(self, db_path: str, query: str):
        self.db_path = db_path
        self.query = query

    def load(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute(self.query)

        rows = cursor.fetchall()
        conn.close()

        return [{
            "text": " | ".join(map(str, row)),
            "source": self.db_path,
            "type": "database"
        } for row in rows]
