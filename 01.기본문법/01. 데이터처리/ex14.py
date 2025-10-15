#복습
#1. 데이터 상수(정수, 실수, 문자열[str], 불린[boold])
#2. 변수: 값을 지정해주는 것
#3. 연산자(산술연산자: +, -, *, /, %, //)
# (관계연산자: >, >=, <, <=, ==, !=)
# (논리연산자: and or not)
#list
names = ['홍길동','심청이','강감찬']

#검색(index: 0, 1, 2) 인덱스 번호를 통해 출력 가능
print(1, names[0])
print(2, names[2])
# print(3, names[3])

#입력(목록 추가: append, insert)
names.append('성춘향')
print(names)
names.insert(0,'박명수')
names.insert(2,'유재석')
print(names)

#수정작업(기존의 값을 다른 값으로 변경)
names[1] = '강호동'
print(names)

#삭제(목록에서 제거)
names.pop() #인덱스 번호 x = 마지막 것 제거 / 인덱스 부여 시 부여번호 삭제
print(names)
names.pop(2)
print(names)

#데이터 글자수 len/ 데이터 위치 count(검색 시 활용)
print(6, len(names))
print(7, names.count('심청이'))
print(8, type(names))