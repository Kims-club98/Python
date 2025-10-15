from db import *
import os

def menuDept():
   os.system('cls') #프롬프트가 초기화되고 새로 작성됨
   while True: 
        print('*'*15,'학과관리','*'*15)
        print('-'*40)
        print('1.등록|2.목록|3.수정|0.종료')
        print('-'*40)
        menu = input('메뉴선택>')
        if menu =='0':
            break

        elif menu=="1":
            dname=input("학과이름>")
            if dname=="":continue
            insertDept(dname)
        elif menu=='2':
            list= listDept()
            for dept in list:
                print(f"학과코드: {dept.dcode}, 학과이름: {dept.dname}")
        elif menu=='3':
            dcode = inputCode('학과코드>',1)
            dept = readDept(dcode)
            dname=input(f"학과이름:{dept.dname}>")
            if dname!="": dept.dname=dname
            
        else:
            print('0~3에서 선택하세요!')

if __name__=='__main__':
    
    menuDept(num)