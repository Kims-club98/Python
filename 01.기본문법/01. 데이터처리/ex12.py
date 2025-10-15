#list 타입 (list도 index, 0부터 시작)
names = ['홍길동', '심청이', '강감찬']
print(names, type(names)) 

names.append('박명수') # names 리스트에서 '박명수'를 추가 append
print(names, type(names))

names. pop() # names 리스트에서 마지막 리스트를 제거 pop
print(names, type(names))

names.insert(1, '박명수') #중간에 '박명수' 추가()
print(names, type(names))

print(names.count('박명수'))

print(names[0]), print(names[-1])
print(names, names[0:2])