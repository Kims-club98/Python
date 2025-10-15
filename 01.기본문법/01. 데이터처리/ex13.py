# 딕셔너리 타입(키값을 통해 가져옴) (중괄호로 값을 가져옴)
students = {1:'홍길동', 2:'심청이', 3:'강감찬'} #중괄호
print(students, type(students))

print(students.get(2)) # get은 students 리스트에서 2번째를 추출
print(students[2]) #students 리스트에서 2번째를 추출

students[4]='박명수' # 추가
print(students, type(students))

print(2 in students) #"키"를 기준으로 키가 있는지를 T/F로 찾아줌

keys = students.keys() #키값만 추출해줌
print(keys, type(keys))

values= students.values() #students 값만 가지고 옴(Keys 값을 가지고 오지 않음, 이름만 가지고 옴)
print(values, type(values))

print('박명수' in values) # values값에 '박명수'가 있는가?
