#숫자인지 체크하는 함수 isnumber
def isnumber(str):
    if str.isnumeric(): #str이 숫자인지 물어보는 함수
        return True # 숫자이면 True
    else:
        print('숫자로 입력하세요!')
        return False #문자이면 False

#. 국어 영어 수학을 입력받아서 평점을 추출

#학점을 구하는 함수 grade(score)
def grade(score): #새로운 함수 정의함(기존 파이썬의 함수를 사용하면 안됨)(함수정의한다: def) _ 정의만 한 상황, 호출을 해야함
    grade = "" #그냥 grade라는 변수명을 만들어줌
    if score >=90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"
    return grade

# 점수를 입력받는 함수 inputNum
def inputNum(title): # 표기법 약속: 2단어(3단어 이상)이상 사용 시, 2번째 단어에는 대문자로 사용(일반적으로는 소문자로 씀)
    while True:
        str = input(f'{title}>') # 타이틀을 입력받아서 작동함
        if str.isnumeric(): #numberic X numeric
            return int(str) # str을 int로 되돌림
        else:
            print(f'{title}을(를) 숫자로 입력하세요!')

# 메뉴 출력하는 함수 (def는 함수 선언) menuPrint
def menuPrint(title):
    print(f'**************{title}***************')
    print('|1.입력|2.검색|3.목록|4.삭제|5.수정|0.종료|')
    print('--------------------------------------')

# 함수의 모음 = 모듈 / 모듈의 모음 = 패키지(03.함수 파일이 패키지)