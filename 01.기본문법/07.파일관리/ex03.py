from function import *

file_name = 'data/juso.txt'
def insert(name, phone, adress):
    with open(file_name, 'a', encoding='utf-8') as file:
        no = int(maxNo()) +1
        file.write(f"{no},{name},{phone},{adress}\n")
        print('등록완료!')

def read():
    with open(file_name, 'r', encoding='utf-8') as file:
        list = [] #list: 데이터를 저장할 변수
        for lines in file.readlines():
            items = lines.split(",") # 칸 구분 ','
            no = items[0]
            name = items[1]
            phone = items[2]
            adress = items[3]
            item = {'no':no, 'name': name, 'phone': phone, 'adress': adress}
            list.append(item) #item을 list에 추가함
        return list

# 이름을 받아 검색결과를 dictonary에 입력함
def search(name):
    items = read()
    list = []
    for item in items:
        if item['name'].find(name) != -1:
            list.append(item)
    return list

#가장 큰 값을 찾아 return하는 함수        
def maxNo(): # no가 0이면 0을 출력, 그 외는 
    items = read()
    nos = []
    for item in items:
        nos.append(item['no'])
    if len(nos) ==0:
        return 0
    else:
        return max(nos)
        
while True:
    menuPrint('주소관리')
    menu = input('메뉴입력>')
    
    if menu =="0": break #종료

    elif menu =='1': #입력
        name = input('성명>')
        if name == "": continue #입력 X 시 다시
        phone = input('전화>')
        adress = input('주소>')
        insert(name, phone, adress)
        
    elif menu =='2':
        items = read()
        name = input('검색이름>')
        list = search(name)
        if len(list) ==0: # 리스트에 없음
            print(f'{name} 데이터가 없습니다!')
            continue
        else: #리스트에 있음
            for item in list:
                print(f"{item['no']}, {item['name']},{item['phone']}, {item['adress']}", end=" ")

    elif menu == '3': #목록
        items = read() #return한 값을 받는 함수는 꼭 list가 아니어도 됨3
        for item in items:
            print(f"{item['no']},{item['name']},{item['phone']}, {item['adress']}", end=" ")
