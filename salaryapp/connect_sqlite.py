import sqlite3
from main import Model

conn = sqlite3.connect('salary.db')
cur = conn.cursor()

cur.execute('SELECT * FROM salary WHERE 1')
print(cur.fetchall())

conn.commit()
conn.close()

conn.execute("INSERT INTO salary VALUES (:id ,:name, :workhour, :salary)"
, {'id':'A02','name':'Yan','workhour':150,'salary':69696969})
