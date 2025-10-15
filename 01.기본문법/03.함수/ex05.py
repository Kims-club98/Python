from fuction import inputNum, grade

kor = inputNum("국어")
eng = inputNum("영어")
mat = inputNum("숫자")
avg = (kor + eng +mat)/3
print(f'평균은 {avg:.2f} 평점은 {grade(avg)}')