import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="karthi710",
    database="rag_demo"
)

print("Connected successfully")
conn.close()
