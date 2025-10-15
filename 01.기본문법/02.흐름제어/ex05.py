#0-100의 합계
tot = 0
for j in range(1,101): #1-100까지
    tot +=j #tot = tot + j (tot를 누적해서 더함)
print(tot)

# 2-100 짝수의 합계
sum=0
for i in range(2,101,2): #2-100을 2씩 누적함
    sum +=i

print(sum)

# 1-99 홀수 합계
sum = 0
for i in range(1,100,2): #1-99 2씩 더함
    sum +=i # sum에 i를 계속 누적함
print(sum)