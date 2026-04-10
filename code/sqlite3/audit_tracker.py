import sqlite3

connection = sqlite3.connect("system_audit.db")
cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        filename TEXT,
        error_count INTEGER,
        date_scanned TEXT
    )
""")

file_name = "server.log"
errors = 12
today = "2026-04-05"

cursor.execute("INSERT INTO logs (filename, error_count, date_scanned) VALUES (?, ?, ?)",
    (file_name, errors, today))

connection.commit()
connection.close()
