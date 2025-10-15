import sqlite3
import os
path = os.path.dirname(os.path.realpath(__file__))
db_name = path + '/juso.db'

con = sqlite3.connect(db_name) #커밋 오픈
cursor = con.cursor()   # DB 오픈(1-7)

sql = 'delete from juso where seq=?'
seq = int(input('삭제번호>'))
cursor. execute(sql, (seq,))
con.commit()

cursor.close()
con. close()