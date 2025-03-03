
import pymysql

conn = pymysql.connect(database = "mindtek", user="root", password="", port=3306)

cursor = conn.cursor()

query = "delete from players where plyid = '484'"

cursor.execute(query)

conn.commit()
conn.close()

