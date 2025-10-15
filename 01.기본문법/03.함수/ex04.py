from fuction import grade, isnumber #외부에서 함수를 가져와서 사용함(ex03 파일에 있는 grade 함수와 isnumber 함수를 가져옴[import])
# *함수를 사용하지 않으면 grde, isnumber가 회색으로 되어있음

while True:
    kor = input('국어>')
    if isnumber(kor):
        break

while True:
    eng = input('영어>')
    if isnumber(eng):
        break

while True:
    mat = input('수학>')
    if isnumber(mat):
        break

avg = (int(kor)+int(eng)+int(mat))/3
level=grade(avg)
print(f'평균:{avg:.2f}, 평점:{level}')