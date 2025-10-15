#다중 for 문 (for문 내 for 문)
# for i in range(5): #0부터 4까지 출력
#     for j in range(5):
#         print(f'({i},{j})') #i도 0~4 출력, j도 0~4 출력
#     print() #행렬을 구분해서 출력해줌(가로: 행, 세로: 열)(행 먼저)

for i in range(1,6,1): #1부터 5까지 1씩 증가
    for j in range(i):
        print("*", end="")
    print()

for i  in range(5,0,-1): #5에서 1까지 차례로 감소
    for j in range(i):
        print("*", end="")
    print()