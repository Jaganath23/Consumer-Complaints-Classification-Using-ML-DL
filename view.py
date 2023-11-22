import sqlite3

conn = sqlite3.connect('best_complaints.db')
c = conn.cursor()

c.execute("SELECT * FROM COMP")
data = c.fetchall()

for d in data:
	print(d)
