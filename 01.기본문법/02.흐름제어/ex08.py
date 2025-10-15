sum =0
while True:
    num = input('숫자입력>')
    if num == "":
        print('프로그램종료')
        break
    sum += int(num)
print('합계:',sum)

# 정리: While True 무한반복 / ""는 아무것도 입력하지 않을 경우를 의미 / break는 계속반복을 멈춤