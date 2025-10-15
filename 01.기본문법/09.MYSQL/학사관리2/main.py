from db import *
from function import *
from dept import *

while True:
    menuPrint('학사관리')
    menu=input('메뉴선택>')
    if menu =='0':
        cur.close()
        con.close()
        print('프로그램을 종료합니다!')

    elif menu =='1': # 입력 >>>? 코드에서 안됨
        stu=Student()
        stu.id=newID()
        print(f'학생학번>{stu.id}')
        stu.name=input('학생이름>')
        if stu.name=="": 
            print('학생 이름을 꼭 입력하세요!')
            continue
        stu.code=inputCode('학생학과>', 1)
        insert(stu)

    elif menu =='2': # 검색
        while True:
            value = input('검색어>')
            if value =="": break
            students = search(value)
            if len(value)==0:
                print('검색 학생이 없습니다!')
            else:
                for stu in students:
                    stu.print()

    elif menu =='3': # 목록
        while True:
            key = inputNum('1. 학번순 | 2. 이름순 | 3. 학과순>')
            if key =="": 
                break # 빠져나가기 엔터
            elif key <1 or key > 3:
                print('1~3번 중에 입력하세요!')
                continue
            students = list(key)
            for stu in students:
                stu.print()

    elif menu =='4': # 삭제
        id=input('학생번호>')
        if id=="": continue
        stu=read(id)
        if stu==None:
            print('삭제할 학생이 없습니다!')
        else:
            stu.print()
            sel = input('삭제하실래요?(Y)>')
            if sel =="Y" or sel =="y":
                delete(id)
        input('아무키나 누르세요!')

    elif menu =='5': # 수정
        id=input('학생번호>')
        stu=read(id)
        if stu==None:
            print('수정할 학생이 없습니다!')
        else:
            stu.print()
            name=input(f"학생이름:{stu.name}>")
            if name!="": stu.name=name
            code=inputCode(f"학생코드:{stu.code}>",5)
            if code!="":stu.code=code
            update(stu)
        input('아무키나 누르세요!')

    elif menu == '6':
        menuDept()

    else:
        print('0~6사이로 입력하세요!')