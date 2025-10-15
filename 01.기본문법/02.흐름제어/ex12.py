#1. 남탕 = 남자이거나, 여자이면서 나이가 4세 미만
#2. 여탕 = 여자이거나, 남자이면서 남이가 4세 미만
# 나이, 성별 받아야함 (while)
#프로그램 무한반복 While 문 (:는 Then 의미)
while True:
    type=input("1.남탕|2.여탕|0.종료>")
    if type == "0":
        print('프로그램을 종료합니다.')
        break
    elif type == "1" or type == "2":
        gender = input('1.남자|2.여자>')
        if type == "1":
            if gender =="1":
                print('남자이므로 입장 가능합니다')
        else:
            age = input('나이>')
            if age < 4:
                print('여자이지만 4시 미만이므로 입장 가능합니다.')
            else:
                print('여자이므로 입장 불가능합니다.')
    else:
        pass