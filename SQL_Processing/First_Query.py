__auth__ = 'NguyenTTin'

import pymysql
#import pymysql.cursors

db = pymysql.connect("localhost", "root", "toor")
cursor = db.cursor()
cursor.execute("show databases;")
data = cursor.fetchall()
print(list(data))

cursor.execute("use mysql;")
cursor.execute("show tables;")
cursor.execute("select* from user;")
data1 = cursor.fetchall()
print(data1)

db.close()