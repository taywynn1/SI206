
import sqlite3

conn = sqlite3.connect('orgdb.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split()
    email = pieces[1]
    org = email.split('@')[1]
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (org,)) #want to pull out the counts for the organization specified
    row = cur.fetchone() #fetches the count result returning it(if more than 1 item pulled, its returned in a tuple) or None when no more data is available
    if row is None: #if the specific org has no counts/nothing returned/no data available, then we insert the org into our database with the count 1
       cur.execute('''INSERT INTO Counts (org, count)
                VALUES (?, 1)''', (org,))
    else: 
        #if we do get a count back/the org exists, then we will updata the count for that org by 1
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',
                    (org,))
    conn.commit() #runs our database

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()