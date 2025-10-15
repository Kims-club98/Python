import sqlite3
import os
path = os.path.dirname(os.path.realpath(__file__))
db_name = path + '/juso.db'

con = sqlite3.connect(db_name) #커밋 오픈
cursor = con.cursor() # DB 호출

sql = "select * from juso" #명령어(SQL 명령)
# sql = "select * from juso where address like '%경'order by seq desc"

cursor.execute(sql)
rows = cursor.fetchall()# 모두 꺼내옴
for row in rows:
    print(f'번호:{row[0]},이름: {row[1]}, 주소:{row[2]}') # sql 출력형태


cursor.close() #커서 종료
con.close() #커밋 종료