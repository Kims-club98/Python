from function import *
from productDB import *

while True:
    menuPrint('상품관리')
    menu=input('메뉴선택>')
    
    if menu=="0": break

    elif menu=="1":
        p = Product()
        p.name = input('상품명>')
        if p.name=="":continue
        p.price=inputNum('상품가격>')
        if p.price=="": p.price = 0
        insert(p)
        print('상품등록완료!')

    elif menu=="2":
        while True:
            value=input('검색어>')
            if value=="": 
                print('검색을 종료합니다.')
                break
            rows = search(value)
            for row in rows:
                rowPrint(row)
    
    elif menu=="3":
        while True:
            type=inputNum('1.코드순 |2.상품이름순 |3. 최저가순 |4. 최고가순')
            if type=="": break
            rows=list(type)
            for row in rows:
                rowPrint(row)

    elif menu=="4":
        code = inputNum('삭제코드>')
        if code=="": continue
        row=read(code)
        p=rowPrint(row)
        sel=input('삭제하실래요?>')
        if sel =="Y" or sel =='y':
            delete(code)
            print('상품삭제완료>')
    
    elif menu=="5":
        code = inputNum('수정코드>')
        if code=="": continue
        row=read(code)
        p=rowPrint(row)
        name = input(f'상품이름:{p.name}>')
        if name!="": p.name=name
        price=input(f'상품가격:{p.price}>')
        if price!="": p.price=price
        sel=input('수정하실래요?(Y)>')
        if sel=="Y" or sel =='y':
            update(p)
            print('수정완료!')

    else:
        print('0~5사이를 입력하세요')
        continue