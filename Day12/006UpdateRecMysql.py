
import pymysql

conn = pymysql.connect(database = "mindtek", user="root", password="", port=3306)

cursor = conn.cursor()

query = "update players set plyname = 'Pusarla Venkata Sindhu' where plyid = '501'"

cursor.execute(query)

conn.commit()
conn.close()

