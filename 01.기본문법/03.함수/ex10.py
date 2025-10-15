# *: 모든 함수 필요 시
from function2 import *

sale = [
    {'code':1, 'name':'냉장고', 'price':250, 'qnt':5},
    {'code':2, 'name':'세탁기', 'price':150, 'qnt':3},
]

while True:
    menuPrint('상품관리')
    menu=input('메뉴선택>')

    if menu =='0':
        print('프로그램을 종료합니다!')
        break
    elif menu=="1":
        new_Code = newCode(sale)
        print(f"상품코드>{new_Code}")
        new_name = input('상품명>')
        if new_name =="":
            continue
        new_price = inputNum('상품단가')
        if new_price =="":
            new_price = 0
        new_qnt = inputNum('상품수량')
        if new_qnt =="":
            new_qnt = 0
        sale.append({'code':new_Code,'name':new_name, 'price':new_price,'qnt':new_qnt})
        print('등록완료!')
        

    elif menu=="2":
        code = inputNum("검색코드")
        idx = search(sale, code)
        if idx == None:
            print(f'{code}번 상품이 없습니다')
        else:
            s = sale[idx] # sale의 리스트 추출
            print(f"상품이름:{s['name']}")
            print(f"상품가격:{s['price']}")
            print(f"상품개수:{s['qnt']}")

    elif menu=="3":
        for s in sale: #sale에서 s를 가져옴
            itemPrint(s) 

    elif menu=="4":
        code = inputNum('삭제코드')
        if code == "":
            continue
        idx = search(sale,code)
        if idx == None:
            print(f'{code}번 상품이 없습니다.')
        else:
            s = sale[idx]
            print(s)
            sel = input('삭제하시겠습니까?(Y)>')
            if sel == "Y" or sel =="y":
                sale.pop(idx)
                print('삭제완료!')
           
    elif menu=="5":
        code = inputNum('수정번호')
        if code == "": continue
        idx = search(sale,code)
        if idx == None:
            print(f'{code}번 상품이 없습니다.')
        s = sale[idx]
        new_name = input(f"상품이름:{s['name']}>")
        if new_name == "": new_name = s['name']
        new_price = inputNum(f"상품가격:{s['price']}만원")
        if new_price =="": s['price']
        new_qnt = inputNum(f"판매수량:{s['qnt']:,}개")
        if new_qnt =="": s['qnt']
        sel = input('수정하실래요?(Y)>')
        if sel == "Y"or sel == "y":
            sale[idx] = {'code':code, 'name':new_name, 'price' :new_price, 'qnt' :new_qnt}
            print('수정완료!')
        

    else:
        print('0~5를 입력하세요!')