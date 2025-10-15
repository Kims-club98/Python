import sqlite3
import os
path=os.path.dirname(os.path.realpath(__file__))
db_name=path + '/juso.db'

class Product:
    def __init__(self):
        self.code = 0
        self.name = ""
        self.price = 0

    def print(self):
        print(f"코드:{self.code}, 이름:{self.name}, 가격:{self.price:,}원")

def list(type): # type =1 코드순, 2. 이름순 3: 최고가, 4: 최저가
    con=sqlite3.connect(db_name) # db open함
    curcor = con.cursor() # 커서 open함
    sql='select * from product' # 순서: code, name, price
    if type == 1:
        sql +=' order by code'
    
    elif type ==2:
        sql +=' order by name'
    
    elif type==3:
        sql +=' order by price'

    elif type==4:
        sql +=' order by price desc' #내림차순
    
    else:
        print('0-4사이로 입력하시오!')

    curcor.execute(sql)
    raws = curcor.fetchall()
    curcor.close()
    con.close()
    return raws

def list_test(type):
    rows = list(type)
    for row in rows:
        p = Product()
        p.code = row[0]
        p.name = row[1]
        p.price = row[2]
        p.print()

#추가: p 객체를 받아 insert
def insert(p): # p = product  / cur = cursar
    con=sqlite3.connect(db_name)
    cur=con.cursor() # check
    sql = 'insert into product(name, price) values(?,?)'
    cur.execute(sql, (p.name, p.price,))
    con.commit()
    cur.close()
    con.close()

# read 코드를 찾기: 코드를 입력받아 row를 입력받음(결과 X 시 None)
def read(code):
    con=sqlite3.connect(db_name)
    cur=con.cursor()
    sql='select * from product where code=?'
    cur.execute(sql,(code,))
    row=cur.fetchall()
    cur.close()
    con.close()
    return row

# search(검색 결과를 출력)
def search(name):
    con=sqlite3.connect(db_name)
    cur=con.cursor()
    sql='select * from product where name like ?'
    cur.execute(sql,(f'%{name}%',))
    rows=cur.fetchall()
    cur.close()
    con.close()
    return rows

# 삭제
def delete(code):
    con=sqlite3.connect(db_name)
    cur=con.cursor()
    sql='delete from product where code=?'
    cur.execute(sql,(code,))
    con.commit()
    cur.close()
    con.close()

#update 수정
def update(p):
    con=sqlite3.connect(db_name)
    cur=con.cursor()
    sql='update product set name=?, price=?, where code=?'
    cur.execute(sql, (p.code, p.price, p.code,))
    con.commit()
    cur.close()
    con.close()
    

#row값을 받아 Print 하는 함수
def rowPrint(row):
    if row ==None:
        print('해당 상품이 없습니다.')
    else:
        product = Product()
        product.code = row[0]
        product.name = row[1]
        product.price = row[2]
        product.print()
        return product    


def insert_test(): # insert 테스트
    p = Product()
    p.name = input("상품이름>")
    p.price = int(input("상품가격>"))
    insert(p)

def read_test(): 
    code=int(input("상품코드>"))
    row = read(code)
    if row==None:
        print('상품코드가 없습니다.')
    else:
        p = Product()
        p.code=row[0]
        p.name=row[1]
        p.price=row[2]
        p.print()

def search_test(): #search 테스트 함수
    while True:
        name=input('상품명>')
        if name =="": break
        rows = search(name)
        for row in rows:
            p = Product()
            p.code = row[0]
            p.name = row[1]
            p.price = row[2]
            p.print()

#삭제 테스트
def delete_test():
    code=int(input("상품코드>"))
    row = read(code)
    if row==None:
        print('상품코드가 없습니다.')
    else:
        p = Product()
        p.code=row[0]
        p.name=row[1]
        p.price=row[2]
        p.print()
        delete(code)
        list_test(1)

def update_test():
    code=int(input('상품코드>'))
    row=read(code)
    p=rowPrint(row)
    if p !=None:
        name=input('상품이름:{p.name}>')
        if name !="": p.name=name
        price=input('상품가격:{p.price}>')
        if price !="":p.price=price
        update(p)
    
        




#테스트용 함수(이 py 내에서만 실행 됨)
if __name__=='__main__':
    update_test()
 