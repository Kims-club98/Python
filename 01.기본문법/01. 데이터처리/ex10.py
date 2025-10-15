#문자열 함수(python은 Index 0번부터 시작)
jumin = '990120-2155011' # 0,1,2,3,4,5,6,7,...
gender = jumin[7]
result = gender == '1' or gender == '3'
#n번째 값을 추출할 때는 '대괄호'를 사용
# 남자 = 7번째가 1 or 3 이어야 함
print(f'{jumin[7]} 결과는 {result}.')

#생년원일을 추출하기
yy=jumin[0:2] #index 2 전까지 추출함(index 0에서 2까지 추출), 0인 경우 yy=jumin[:2]로 0 생략 가능
print(yy)

mm=jumin[2:4] #index 2에서 4전까지 추출 
print(mm)

dd=jumin[4:6]
print(dd)
print(f'{yy}년{mm}월{dd}일')

print(jumin[-1:]) #반대서부터 출력을 원할 경우 다음 문자열에 대해서는 마지막이 -7임