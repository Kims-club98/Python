from fuction import menuPrint, inputNum
sale =[
    {'code':1, 'name':'냉장고','price':250,'qnt':5},
    {'code':2, 'name':'세탁기','price':150,'qnt':3},
]

#검색함수(코드를 찾으면 Print됨)
def search(code):
    isFind = False # 찾기 이전
    for index, s in enumerate(sale): ##???
        if s['code'] ==code: # s['code']에서 code를 찾은 경우 /code가 
            isFind = True # Code를 찾은 경우
            sum = s['price']* s['qnt'] #sum 은 list의 'price' * 'qnt'(개수)임 sum 변수설정
            print(s['code'], s['name'], s['price'], s['qnt'], sum) #출력값
        
    if isFind == False: #찾기를 진행했으나, 찾지 못한 경우
        print('상품이 존재하지 않습니다.')
    return isFind
    

# 목록함수(3번): 모든 데이터를 출력해줌
def list():
    for index, s in enumerate(sale):
        sum = s['price']* s['qnt'] 
        print(s['code'], s['name'], s['price'], s['qnt'], sum)
    if len(sale)==0:
        print('상품이 존재하지 않습니다.')
    else:
        print('상품이 존재합니다.')

# 삭제함수 (del)
def delete(code):
    isFind = search(code)
    if isFind == True: # True 의 Index 번호를 알아야 함
        for index, s in enumerate(sale):
             if s['code'] == code:
                sale.pop(index)
                print("삭제성공!")

#입력함수
def insert():
    codes = []
    for s in sale:
        codes.append(s['code'])
    new_code = max(codes) +1

    code = print(f"상품코드>{new_code}") #정수 입력
    name = input("상품이름>") #문자열 입력
    price = inputNum("상품가격")
    qnt = inputNum("판매수량")
    sale.append({'code':code, 'name':name, 'price':price, 'qnt':qnt})
    print("등록성공")



while True:
    menuPrint('상품매출관리')
    menu = input("메뉴선택>")

    if menu == "0":
        print('프로그램을 종료합니다.')
        break

    elif menu == "1": #입력
        insert()
        
    elif menu == "2": #검색
        code =inputNum("검색코드")
        search(code)
        
    elif menu == "3": #목록
        list()

    elif menu == "4": #삭제
        code = input("삭제코드>")
        delete(code)

    elif menu == "5": #수정
        pass