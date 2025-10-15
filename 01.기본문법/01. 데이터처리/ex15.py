# 딕셔너리 dict (키값, 중괄호) 1: 이름
students = {1: '홍길동', 2:'강감찬', 3:'이순신'}
print(1,type(students))

#검색(get)
print(2, students.get(2))
print(2, students.get(4)) # 없는 값 = None 출력

#입력
students[5] = '유재석'
print(3, students)

#수정
students[1] = '김길동'
print(4, students)
# 새로운 칸 입력 시 추가 / 기존 칸에 이름 시 변경

#삭제 pop
students.pop(2)
print(5, students)

#데이터 전부삭제 Clear
students.clear()
print(6, students)