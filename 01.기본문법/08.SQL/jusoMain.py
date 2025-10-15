from function import *
from jusoDB import *

while True:
    menuPrint('주소선택')
    menu = input('메뉴선택>')
    if menu =="0":
        break

    elif menu =="1": #입력
        pass

    elif menu =="2": #검색
        pass

    elif menu =="3": # 목록
        for row in rows:
            perosn=Person()
            perosn.seq=Person()
            perosn.name=Person()
            perosn.address=Person()
            perosn.print()

    elif menu =="4": # 삭제
        pass

    elif menu =="5": #수정
        pass

    else:
        print('0~5사이를 입력하세요!')