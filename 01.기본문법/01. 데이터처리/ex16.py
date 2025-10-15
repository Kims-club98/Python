#튜플(tuple) 소괄호 (list 대괄호, dict 중괄호, tuple 소괄호)
# tuple은 수정/삭제가 불가하지만, 빠름(검색전용)
menu = ('돈가스', '치즈가스')
print(1, menu, type(menu))
print(2, menu[1]) #없는 자료 시 error

(name, age, hobby) = ('김종국', 20, '코딩')
print(f'이름은 {name}, 나이는 {age}, 취미는 {hobby}.')

