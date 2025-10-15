#DB에 Insert 하는 과정
import sqlite3
import os
path = os.path.dirname(os.path.realpath(__file__))
db_name = path + '/juso.db'

con = sqlite3.connect(db_name) #커밋 오픈
cursor = con.cursor() #커서 연결

sql = "insert into juso(name, address) values('강감찬','부산시 동래구')"
cursor.execute(sql)
sql = "insert into juso(name, address) values('홍길동','경기도 광명시')"
cursor.execute(sql)
sql = "insert into juso(name, address) values('이순신','부산신 해운대구')"
cursor.execute(sql)

id = cursor.lastrowid

con.commit()
cursor.close() # 커서 클로즈
con.close() # 커밋 클로즈

print(f'id:{id}')
