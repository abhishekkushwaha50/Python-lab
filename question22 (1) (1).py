import sqlite3

conn = sqlite3.connect("test.db")
cur = conn.cursor()

cur.execute("INSERT INTO student VALUES (1, 'John')")
cur.execute("UPDATE student SET name='Mike' WHERE id=1")
cur.execute("SELECT * FROM student")
print(cur.fetchall())
cur.execute("DELETE FROM student WHERE id=1")

conn.commit()
conn.close()