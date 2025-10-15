from function import *
from database import *

while True:
    menuPrint('학생관리')
    menu = input('메뉴선택>')

    if menu=='0': 
        print('프로그램을 종료합니다!')
        cur.close()
        con.close()
        break

    elif menu=='1': #입력
        stu = Students()
        stu.id=newID()
        print(f'학번>{stu.id}')
        while True:     
            stu.name=input('이름>')        
            if stu.name=="":
                print('이름을 반드시 입력하세요')
                continue
            else:
                break
        stu.dept = inputDept('학과코드>',1)
        insert(stu)
        print('학생등록성공!')

        insert(stu)
        print('학생등록성공!')
            
    elif menu=='2': # 검색
        while True:
            value = input('검색어>')
            if value =="": break
            students=search(value)
            if len(students)==0:
                print('검색결과가 없습니다!')
                continue
            for stu in students:
                stu.print()
            print(f'총 {len(students)}명이 검색되었습니다.\n')

    elif menu=='3': # 목록
        students = list()
        for stu in students:
            stu.print()
        print(f'총{len(students)} 명의 학생이 존재합니다.')

    elif menu=='4': # 삭제?? 오류
        id=input("학번>")
        if id=="":continue
        stu=read(id)
        if stu==None:
            print('삭제할 학생이 없습니다.')
        else:
            stu.print()
            sel = input('삭제하실래요?(Y)>')
            if sel=="Y" or sel =="y":
                delete(id)
                print('삭제완료!')

    elif menu=='5': # 수정
        id=input("학번>")
        if id=='':continue
        stu=read(id)
        if stu==None:
            print('수정할 학생이 없습니다.')
            continue
        stu.print()
        name=input(f'이름:{stu.name}>')
        if name !="": stu.name=name
        dept = inputDept('학과코드:{stu.dept}>')
        update(stu)
        print('수정완료')


    else:
        print('0~5사이를 입력하시오!')
    