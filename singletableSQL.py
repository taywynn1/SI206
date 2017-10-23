import sqlite3

conn = sqlite3.connect('ages.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Ages')
cur.execute('CREATE TABLE Ages (name VARCHAR, age INTEGER)')

cur.execute('DELETE FROM Ages;')
cur.execute('INSERT INTO Ages(name,age) VALUES ("Jayse", 14)')
cur.execute('INSERT INTO Ages(name,age) VALUES ("Bella", 13)')
cur.execute('INSERT INTO Ages(name,age) VALUES ("Athena", 38)')
cur.execute('INSERT INTO Ages(name,age) VALUES ("Caitlinn", 27)')
cur.execute('INSERT INTO Ages(name,age) VALUES ("Catriona", 31)')
cur.execute('INSERT INTO Ages(name,age) VALUES ("Cohen", 21)')

cur.execute('SELECT hex(name || age) AS X FROM Ages ORDER BY X')

conn.commit()
for row in cur:
	print(row)
	break

cur.close()

conn.close()