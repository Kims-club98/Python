from db import *
from classes import *

# 리스트를 출력해주는 함수
def list():
    try:
        sql='select * from product'
        cur.execute(sql)
        rows=cur.fetchall()
        products=[]
        for row in rows:
            product=Product()
            product.code=row['code']
            product.name=row['name']
            product.price=row['price']
            products.append(product)
        return products
    except Exception as err:
        print("리스트 함수 오류", err)

def insert(product):
    try:
        sql='insert into product(code, name, price) values(%s,%s,%s)'
        cur.execute(sql,(product.code,product.name,product.price))
        con.commit()
        print('상품등록완료!')
    
    except Exception as err:
        print('등록 함수 오류',err)

def search(value):
    try:
        sql='select * from product where code like %s or name like %s'
        cur.execute(sql,(f"%{value}%", f"%{value}%"))
        rows=cur.fetchall()
        products=[]
        for row in rows:
            product=Product()
            product.code=row['code']
            product.name=row['name']
            product.price=row['price']
            products.append(product)
        return products
    except Exception as err:
        print('찾기함수오류',err)

def read(code):
    try:
        sql =f'select * from product where code={code}'
        cur.execute(sql) 
        row=cur.fetchone()
        if row !=None:
            product = Product() 
            product.code = row['code']
            product.name=row['name']
            Product.price=row['price']
            return product

    except Exception as err:
        print('상품읽기 오류', err)

#inputCode 조건: 번호 3자리 이상, 숫자입력 필수
def inputCode(title):
    while True:  #무한반복
        code=input("상품코드>")
        if code=="": return code
        if len(code)!=3:
            print('상품번호는 3자리로 입력하세요')
        elif not code.isnumeric():
            print('상품을 숫자로 입력하세요')
        else:
            return code
         
def inputPrice(title):
    while True:
        price = input(title)
        if price =="":
            return 0
        elif not price.isnumeric():
            print('가격을 숫자로 입력하세요!')
        else:
            return int(price)    

# 수정함수
def update(product):
    try:
        sql= "update product set name=%s, price=%s where code=%s"
        cur.execute(sql,(product.name, product.price, product.code))
        con.commit()
        print('상품수정완료!')
        
    except Exception as err:
        print('수정함수오류',err)

#숫자를 입력받는 함수

def inputNum(title):
    while True:
        str = input(title)
        if str.isnumeric():
            return int(str)
        
        elif str == "":
            return str
        
        else:
            print('숫자로 입력하세요!')

        

if __name__=='__main__':
    price = inputPrice('상품가격>')
    print("상품가격:",price)