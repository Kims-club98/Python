no = int(input('학생수>'))

names =[] #dict
for i in range(no): # 1- no-1까지
    name = input('이름>')
    names.append(name)

for i in range(len(names)):
    print(i, names[i], end=',')
print()

for i, name in enumerate(names):
    print(i,name, end=',')