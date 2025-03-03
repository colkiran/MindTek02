
import pymysql

conn = pymysql.connect(database = "mindtek", user="root", password="", port=3306)

cursor = conn.cursor()

FL = open("players.txt", "r")
for line in FL.readlines():
    cursor.execute(line)

FL.close()

conn.commit()
conn.close()

