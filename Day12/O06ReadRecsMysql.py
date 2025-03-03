
import pymysql
from prettytable import from_db_cursor


conn = pymysql.connect(database = "mindtek", user="root", password="", port=3306)

cursor = conn.cursor()

cursor.execute("select * from players")

prtyTbl = from_db_cursor(cursor)

# for row in cursor.fetchall():
#     print(row)

conn.commit()
conn.close()

prtyTbl.align['plyname'] = 'l'
prtyTbl.align['acheivement'] = 'l'
prtyTbl.align['sport'] = 'l'

print(prtyTbl)

