import sqlite3

conn = sqlite3.connect("internship.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS student(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT,
email TEXT,
password TEXT,
department TEXT,
cgpa REAL,
skills TEXT,
interest TEXT,
location TEXT
)
""")

conn.commit()

conn.close()

print("Database Created Successfully")