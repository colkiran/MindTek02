
import pymysql

conn = pymysql.connect(user="root", password="", port=3306)

cursor = conn.cursor()

query = "create database mindtek"

cursor.execute(query)

conn.close()

