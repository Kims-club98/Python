# 집합(set) 중괄호 {} dict는 키와 값 / set는 값만
# 교집합, 합집합 사용
java = {'유재석', '홍길동', '심청이'}
print(1, java, type(java))

python = {'심청이', '이순신', '강호동'}
print(2, python, type(python))

print(3, java.intersection(python)) #교집합 intersection
print(4, java.union(python)) #합집합 union (java or Python)
print(5, java.difference(python)) #차집합 Java만 할 수 있는 사람
print(6, python.difference(java)) # Python만 할 수 있는 사람
java.add('강호동') #추가
print(7, java)
java.remove('유재석') #집합에서 삭제 remove
print(8, java)
java.clear() #전부 제거 clear
print(9, java)