import os
path = os.path.dirname(os.path.realpath(__file__))
# print('현재패스:', path)

#주소 관리를 위한 class 클래스명은 대문자)(클래스 - 생성자, 매서드 O)
class Person:
    def __init__(self): # 생성자는 이름이 정해짐
        self.seq = 0 # Class 의 속성1
        self.name = "" # Class 의 속성2
        self.address = "경기 광명"#초기값을 지정 가능 # Class 의 속성3 
        
    def print(self): #매서드(함수)
        print(f"번호:{self.seq},이름:{self.name},주소: {self.address}")
        print('-' * 50)

file_name = path + '/juso.txt'

def fileAppend(list):
    with open(file_name, 'a', encoding='utf-8')as file:
        file.write(f'{list.seq},{list.name},{list.address}\n')

#파일에 객체를 추가하는 함수
def fileAppend(person):
    with open(file_name, 'a', encoding='utf-8') as file:
        file.write(f'{person.seq},{person.name},{person.address}\n')

# 파일에 객체를 추가하는 함수 (person을 받아 file에 추가)
def fileWrite(list):
    with open(file_name, 'w', encoding= 'utf-8') as file:
        for person in list:
            file.write(f"{person.seq}, {person.name}, {person.address}\n")

#파일에서 date를 읽어오는 함수
def fileRead():
    list = []
    with open(file_name, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        for line in lines:
            items = line.split(',')
            person =Person()
            person.seq = int(items[0])
            person.name = items[1]
            person.address = items[2].replace('\n',"")
            list.append(person)
        return list
    
#fileRead() 함수 테스트
def list():
    list = fileRead()
    for person in list:
        person.print()

#데이터 추가
def append():
    person = Person()
    person.seq = 5
    person.name = '이순신'
    person.adress = '인천 서구 경서동'
    person.print()
    fileAppend(person)

def search(type, value):
    list = fileRead()
    result = []
    if type == 1: # seq 검색
        if value == person.seq:
            result = [person for person in list if person.seq == value]
        elif type == 2: #name 검색
            result = [person for person in list if person.name.find(value)!=-1]
        elif type == 3: # adress 검색
            result = [person for person in list if person.name.find(value)!=-1]
        return result
    
# 삭제함수
def delete(seq):
    list = fileRead()
    result = [perosn for perosn in list if perosn.seq != seq]
    fileWrite(result)

# 수정함수(update) - person 객체를 받아냄
def update(person):
    list = fileRead()
    result = [person for person in list if person.seq== seq]
    if len(result) == 0:
        print('검색결과가 없습니다.')
    else:
        person = result[0]
        # person.print()
        name = input(f'이름:{person.name}>')
        if name != '': person.name = name
        address = input(f'주소: {person.address}>')
        if address !="": person.address=address
        fileWrite(list)
        person.print()




