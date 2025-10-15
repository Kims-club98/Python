from productFile import *
from function import *

def newCode():
    list = fileRead()
    if len(list)==0: return 1
    codes = [product.code for product in list]
    return max(codes) +1

def search(code):
    list = fileRead()
    result = [p for p in list if p.code == code]
    if len(list) ==0:
        return result[0]

while True:
    menuPrint('상품관리')
    menu = input('메뉴선택>')
    if menu =="0":
        print('프로그램을 종료합니다.')
        break

    elif menu=='1': #입력
        product = Product()
        product.code = newCode()
        print(f'코드번호>{product.code}')
        product.name = input('이름>')
        if product.name == "": continue
        product.price = inputNum('가격>')
        fileAppend(product)
        product.print()
        

    elif menu=='2': # 검색
        # while True:
        #     value = inputNum('검색어>')
        #     if value =="": break
        # list = fileRead()
        # result = [p for p in list if p.code.find(value) !=-1 or p.name.find(value)!=-1]
        # if len(result) ==0:
        #     print('검색내용이 없습니다.')
        #     continue
        # for product in result:
        #     product.print()

        code= inputNum('검색할 상품코드 입력하세요>')
        list = fileRead()
        result= [p for p in list if p.code == code]
        if result:
                result[0].print()
        else:
            print('해당 코드의 상품이 없습니다.')

    elif menu=='3': # 목록
        while True:
            sort = inputNum("1.코드순|2.이름순|3.최저가|4.최고가>")
            if sort == '': break
            list = fileRead()
            result =[]
            if sort == 1: # sort 정렬함
                result=sorted(list, key=lambda p:p.code) # 코드의 오름차순
            if sort == 2:
                result=sorted(list, key=lambda p:p.name) # 이름의 오름차순
            if sort == 3:
                result=sorted(list, key=lambda p:p.price) # 가격의 오름차순
            if sort == 4:
                result=sorted(list, key=lambda p:p.price,reverse=True) # 가격의 내림차순
                print()

            for p in result:
                p.print()


    elif menu=='4': # 삭제
        seq = inputNum('삭제번호>')
        list = fileRead()
        result =[p for p in list if p.code==seq]
        if len(result) ==0:
            print('삭제할 번호가 없습니다.')
            continue
        product = result[0]
        product.print()
        sel = input('삭제하시겠습니까?(Y)>')
        if sel =='Y' or sel == 'y':
            result = [p for p in list if p.code!=seq]
            fileWrite(result)
            print('삭제성공!')
        


    elif menu=='5': #수정
        seq = inputNum('수정번호>')
        if seq == "": continue
        list = fileRead()
        result = [p for p in list if p.code==seq]
        if len(result)==0:
            print('번호가 없습니다.')
            continue
        product = result[0]
        name = input(f'이름{product.name}>')
        if name !="":
            product.name=name
        price = input(f'가격{product.price}>')
        if price !="":
            product.price=price
        sel = input('수정하시겠습니까?(Y)>')
        if sel =='Y' or sel =='y':
            product.print()
            fileWrite(list)
            print('수정완료')        
        
    else:
        print('0~5까지 입력하세요.')
        continue

