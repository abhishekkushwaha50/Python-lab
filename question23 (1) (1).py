import sqlite3

conn = sqlite3.connect("test.db")
cur = conn.cursor()

try:
    cur.execute("INSERT INTO student VALUES (2, 'Alice')")
    conn.commit()
except:
    conn.rollback()

conn.close()