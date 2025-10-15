import os
path = os.path. dirname(os.path.realpath(__file__))
# print('현재패스', path)
file_name = path +'\product.txt'
# print('파일명',file_name)

class Product:
    def __init__(self):
        self.code = 0
        self.name = ""
        self.price = 0

    def print(self):
        print(f'코드:{self.code},상품명:{self.name},가격:{self.price:,}원')
        print('-'*50)

#데이터 하나 추가 함수
def fileAppend(p): #p = product 객차 함수
        with open(file_name, 'a',encoding='utf-8') as file:
            file.write(f'{p.code},{p.name},{p.price}\n')

#모든 데이터를 읽는 함수
def fileRead():
     with open(file_name, 'r',encoding='utf-8') as file:
        list = []
        lines = file.readlines()
        for line in lines: #하나씩 확인해 출력
            items = line.split(',') #items는 list
            p = Product()
            p.code = int(items[0])
            p.name = items[1]
            p.price = int(items[2].replace('\n',"")) #이전 형식에서 빈 공백으로 + int 형식으로 변경
            list.append(p)
        return list
     
#모든 데이터를 다시 쓰기 함수(if 2개 데이터를 지웠다 다시 씀)
def fileWrite(list):
      with open(file_name, 'w',encoding='utf-8') as file: #txt 파일에서 가져옴
           for p in list:
                file.write(f'{p.code},{p.name},{p.price}')

#모든 데이터를 삭제하는 함수
def delete(code):
     list = fileRead()
     result = [p for p in list if p.code !=code]
     fileWrite(result) #삭제 
     
def list():
     list = fileRead()
     for p in list: # 모든 자료를 list로 이동, 그리고 print
          p.print()

#수정하는 함수
def update():
     code=1
     list = fileRead()
     result = [p for p in list if p.code == code]
     p = result[0]
     p.name = '아무개'
     fileWrite(list)



def append():
        p = Product()
        p.code = 2
        p.name = '에어컨'
        p.price = 700
        fileAppend(p)
        print('등록성공!')




     