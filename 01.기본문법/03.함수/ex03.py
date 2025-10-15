# 수학 점수 입력 시 숫자를 입력할때까지 입력하는 것
#step 1. 숫자인지를 체크(숫자 시 True return, 문자 시 False)

#숫자인지 체크하는 함수
def isnumber(str):
    if str.isnumeric(): #str이 숫자인지 물어보는 함수
        return True # 숫자이면 True
    else:
        print('숫자로 입력하세요')
        return False #문자이면 False

#. 국어 영어 수학을 입력받아서 평점을 추출

#학점을 구하는 함수
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

while True:
    score = input("점수>")
    if score=="": #score에 아무것도 입력하지 않았을 때
        break #프로그램 종료
    if isnumber(score): # score가 숫자인 경우
        level = grade(int(score))
        print(f'평점:{level}')
    
    #Q. 근데 왜 문자 입력하면 점수로 Back 하나???


