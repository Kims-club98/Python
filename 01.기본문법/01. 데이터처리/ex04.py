num1 = input('숫자1>')
num2 = input('숫자2>')
num1 = int(num1)
num2 = int(num2)
# input은 항상 문자열을 추출함 So 정수/실수가 필요한 경우에는 int()를 통해 만들어줘야 print에서 오류가 발생하지 않음

add = num1 + num2
# 산술연산자
print(f'{num1}+{num2}={add}')
print(f'{num1}-{num2}={num1-num2}')
print(f'{num1}*{num2}={num1*num2}')
print(f'{num1}/{num2}={num1/num2:.2f}')
print(f'{num1}%{num2}={num1%num2}')
# %연산자: 나머지 num1에서 num2로 나눈 후 나머지
print(f'{num1}//{num2}={num1//num2}')
# //연산자: num1 에서 num2로 나눈 후 몫.