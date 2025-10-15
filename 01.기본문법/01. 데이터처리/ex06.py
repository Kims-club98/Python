#논리연산자(and, or, not)
age = 20
gender = '남'
# Q. 남자면서 나이가 20세 이상인 경우 입장가능(true) 불가능(false)
result1 = (age >= 20)
print(1, result1)

result2 = (gender == '남')
print(2, result2)

result3 = (result1 and result2)
print(3, result3)
result4 = (result1 or result2)
print(4, result4)