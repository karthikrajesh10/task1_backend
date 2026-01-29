import mysql.connector
from tts_stt_backend.rag.loaders.base import BaseLoader


class MySQLLoader(BaseLoader):
    def __init__(self, host, user, password, database, query):
        self.config = {
            "host": host,
            "user": user,
            "password": password,
            "database": database
        }
        self.query = query

    def load(self):
        conn = mysql.connector.connect(**self.config)
        cursor = conn.cursor()
        cursor.execute(self.query)

        rows = cursor.fetchall()
        columns = [col[0] for col in cursor.description]

        documents = []

        for row in rows:
            text = " | ".join(
                f"{col}: {val}" for col, val in zip(columns, row)
            )

            documents.append({
                "text": text,
                "source": "mysql:students",
                "type": "database"
            })

        cursor.close()
        conn.close()
        return documents
