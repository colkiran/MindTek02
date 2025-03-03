
import pymysql

conn = pymysql.connect(database = "mindtek", user="root", password="", port=3306)

cursor = conn.cursor()

query = """
create table players (
plyid varchar(7) PRIMARY KEY,
plyname varchar(50) not null, 
sport varchar(30) not null, 
acheivement varchar(50) not null
)
"""
cursor.execute(query)

conn.close()

