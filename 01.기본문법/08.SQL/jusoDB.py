import sqlite3
import os
path = os.path.dirname(os.path.realpath(__file__))
db_name=path+'/juso.db' #주소 위치 지정

class Person:
    def __init__(self): # 생성자(__init__)
        self.seq =0
        self.name ="홍길동"
        self.address="경기도 광명시"

    def print(self):
        print(f'번호:{self.seq}, 이름:{self.name}, 주소:{self.address}')

#목록출력함수
def list_all():
    con =sqlite3.connect(db_name)
    cursor = con.cursor
    sql = 'select seq, name address from juso'
    cursor.execute(sql)
    rows = cursor.fetchall()
    cursor.close()
    con.close()
    return rows

#읽기
def read(seq):
    con = sqlite3.connect(db_name)
    cursor= con.cursor()
    sql ="select * from juso where seq=?"
    cursor.execute(sql,(sql,))
    row = cursor.fetchone()
    cursor.close()
    con.close()
    return row #번호를 받아 잃어오는 함수

#삭제
def delete(seq):
    con = sqlite3.connect(db_name)
    cursor= con.cursor()
    sql ="delete from juso"
    delete(sql, (sql,))
    cursor.commit()
    cursor.close()
    con.close()

# 입력 insert
def insert(person):
    con = sqlite3.connect(db_name)
    cursor= con.cursor()
    sql ="insert into juso(name, address) values(?,?)"
    cursor.execute(sql, (person.name, person.address,))
    cursor.commit() # delete, insert, update에 사용
    cursor.close()
    con.close()

# 업데이트문 update
def update(person):
    con = sqlite3.connect(db_name)
    cursor= con.cursor()
    sql ="update juso set name=?, address=? where seq=?"
    cursor.execute(sql,(person.name, person.address, person.seq,))
    cursor.commit() # delete, insert, update에 사용
    cursor.close()
    con.close()




if __name__=='__main__':
    p = Person()
    p.seq = int(input("수정번호>"))
    row = read(p.seq)
    if row == None:
        print('수정번호가 없습니다.')
    else:
        p.name = row[1]
        p.address=row[2]
        name = input(f'이름:{p.name}>')
        if name != "": p.name=name

        address = input(f'주소:{p.address}>')
        if address != "": p.address = address
        update(p)
        print('수정완료!')