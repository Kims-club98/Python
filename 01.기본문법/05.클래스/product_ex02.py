from function import *
from product import Product

products = [
    {'code':'001', 'name':'LG 냉장고','price':180},
    {'code':'002', 'name':'LG 세탁기','price':150},
]

def search(code):
    for idx, p in enumerate(products):
        if code == p['code']:
            return idx

while True:
    menuPrint('상품관리')
    menu = input('메뉴선택>')
    if menu == "0": break

    elif menu == "1": #등록
        code = len(products)+1
        code= f'{code:03d}'
        name = input('상품명>')
        if name == "":
            continue
        price = input('상품가격>')
        if price == "":
            price = 0

        p = Product(code, name, price) # 유효성 체크 필요(실제는)
        products.append(p.dict())
        print('상품등록완료!')

    elif menu =='2': #검색
        name = input('검색이름>')
        for p in products:
            if p['name'].upper().find(name.upper()) != -1:
                print(p['code'], p['name'], p['price'])


    elif menu == '3': #목록
        for p in products:
            print(p['code'], p['name'],p['price'])
        print(f'{len(products)}개 상품이 존재합니다.')

    elif menu == '4': #삭제
        code = input('삭제코드>')
        if code == "": continue #코드에 공란 기입
        idx = search(code)
        if idx == None: #상품 없음
            print(f'{code}번 상품이 없습니다.')
        else: #상품 찾음
            p=products[idx]
            print[p['code'],p['name'],p['price']]
            sel = input("삭제할래요?>")
            if sel == "Y" or sel == "y":
            products.pop(idx)
            print('상품삭제완료!')
    
    elif menu == '5': #수정
        code = input('수정코드>') #수정코드 입력
        if code == "": continue
        idx = search(code)
        if idx == None:
            print(f'{code}번 상품이 없습니다') 
            continue
        p = products[idx]
        name = input(f"수정이름:{p['name']}>") #수정이름 입력
        if name != '': p['name'] = name

        price = inputNum(f"상품가격:{p['price']}>") #수정가격 입력
        if price == "": p['price'] = price
        print('오류검토완료!')
