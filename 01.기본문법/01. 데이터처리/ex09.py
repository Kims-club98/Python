# 기본함수 1: 절대값(abs())
print(1, abs(-5))

# 기본함수 2: 거듭제곱(pow())
print(2, pow(2,3)) # 2의 3승 = 8

# 기본함수 3: 최대값(Max()) / 최소값(Min())
print(3, max(2,3,10,5,7))
print(4, min(1,2,10,3,7,-5))

# 기본함수 4: 반올림(Round())
print(5, round(3.14)) # 정수까지 반올림(따로 뒷자리 지정 X 경우)
print(6, round(3.141592,3)) # 3째 자리까지 출력

# 올림, 버림(floor)(기본함수 아님) from math import * 모든 math 함수에서 가져온다
from math import *
print(7, floor(4.99)) #내림
print(8, ceil(3.14)) #올림
print(9, sqrt(16)) #제곱근

# random 함수(random, randint)
from random import * #Random에 있는 함수에 모두를 가져오겠다
print(10, random()) #Random한 글자가 나옴 0<= random <1
print(11, random()*10) #Random한 글자가 나옴 0<= random <10
print(12, int(random()*10)) #int로 정수를 만들어줘서 0<=random <=9까지 출력됨
print(13, randint(1, 45)) #1-45번까지 숫자 중 하나를 랜덤하게 추출