#문자열 함수( lower, upper, capitalize, islower, isupper)
str = 'Python is Amazing' # 변수지정
print(1, str.lower()) # 문자열을 소문자로 출력
print(2, str.upper()) # 문자열을 대문자로 출력
print(3, str.capitalize()) #문자열의 첫 글자만 대문자로 출력
print(4, str[0].islower()) #문자열의 글자가 소문자인가? T/F 추출
print(5, str[0].isupper()) #문자열의 크기가 대문자인가? T/F 추출
print(6, len(str)) #str의 글자 길이 추출
print(7, str.replace('Python', '파이썬')) #앞의 단어를 뒤의 단어로 교체해줌

index = str.index('a') #index값에서 a의 위치를 가져옴
print(8, index) # a 가 몇 번째에 있는지 추출 단, 없는 경우에는 '오류' 표시(find는 없는 경우 -1 출력)
print(9, str[index:]) #index 가 정수에서 문자열로 변환됨
print(10,str[index:].upper()) #index에서 문자열로 변환되고, 대문자로 변환
print(11, str.find('ab')) #index에서 ab의 위치를 찾아줌, 단 오류 시 -1로 출력
print(12, str.count('i')) #str 함수에서 'i'의 개수
print(13, str.count('easy')) #str 함수에 없는 문자열의 경우 '0'이 추출됨
