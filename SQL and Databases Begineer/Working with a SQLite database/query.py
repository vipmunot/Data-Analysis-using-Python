import sqlite3
conn = sqlite3.connect('factbook.db')
c = conn.cursor()
c.execute('select name from facts order by population asc limit 10;')
print(c.fetchall())


