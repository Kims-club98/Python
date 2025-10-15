from db import *
from classes import *


def sale_list(value):
    try:
        sql='select * from view_sale where code like %s or name like %s'
        value=f'%{value}%'
        cur.execute(sql,(value,value))
        rows=cur.fetchall()
        sales=[]
        for row in rows:
            sale = Sale()
            sale.seq=row['seq']
            sale.code=row['code']
            sale.name=row['name']
            sale.date=row['date']
            sale.price=row['price']
            sale.qnt=row['qnt']
            sale.sum=row['price'] * row['qnt']
            sales.append(sale)
        return sales

    except Exception as err:
        print('세일 리스트 함수 오류',err)

def sale_insert(sale):
    try:
        sql='insert into sale(code, date, qnt, price) values(%s, now(), %s, %s)'
        cur.execute(sql,(sale.code, sale.qnt, sale.price))
        con.commit()
        print('매출등록완료!')
    except Exception as err:
        print('세일 Search값 오류', err)


if __name__=='__main__':
    sales=list()
    for sale in sales:
        sale.print()