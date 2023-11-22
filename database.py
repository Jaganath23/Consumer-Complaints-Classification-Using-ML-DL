import sqlite3

conn = sqlite3.connect('complaints.db')

c= conn.cursor()
c.execute('''CREATE TABLE COMP
             ([user_comp] text,[category] text)''')

conn.commit()