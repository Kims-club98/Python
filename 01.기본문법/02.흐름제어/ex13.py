# for 문 (1-10 출력) range를 통해 일정한 수를 변경 가능함
# for 숫1 in 숫2
for i in range(10):
    if i<9:
        print(i, end=",")
    else:
        print(i)
for i in range(2,11,2): # 원하는 범위에서 +1, 12까지 원하면 13입력
    print(i, end=",")
for i in range(2, 10, 2):
    print(i, end=',')

#name을 통해 여러 변수 입력(list 타입)
names = ['apple', 'banna']
for name in names:
    print(name)