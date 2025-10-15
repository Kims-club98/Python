# 함수 정의
#Q. 성적을 입력 시 그것에 맞는 함수를 추출
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
    print(f'점수는 {score}점, 학점은 {grade} 입니다.') #일단 넘어감

grade(90) #점수를 호출
grade(30)

while True:
    score = input("점수:종료0>")
    if not score.isnumeric(): # score가 숫자가 아닌 경우
        print('숫자로 입력하세요')
        continue #다시 while문으로 이동
    if score =="0": # 숫자가 '0'인 경우
        print('프로그램을 종료합니다.')
        break # 프로그램 종료
    else: #나머지 숫자가 아닌경우, 0인경우를 제외
        grade(int(score)) #score을 표시 
