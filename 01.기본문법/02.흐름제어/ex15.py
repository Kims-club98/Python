#한줄 for 문(반복문 for)
temp =[i for i in range(1, 11)] # 대괄호는 type 은 list temp는 1에서 10까지를 출력함(대괄호이므로 타입은 list)
print(temp, type(temp))

even = [i for i in temp if i%2==0] #even은 temp에서 2로 나눌 시 나머지 0이 되는 것을 추출
print(even)

odd = [i for i in temp if i%2==1]
print(odd)

result = ['짝수' if i%2==0 else '홀수' for i in temp] #temp에서 꺼내서 2로 나누어 나머지가 0이면 '짝수 출력, 나머지는 '홀수' 출력
print(result)

names = ['Iron man','Chirs,','Justin Hwang']
names = [len(name) for name in names] # names에서 name을 추출하며, name에서 소문자로 추출함(.lower)/첫글자만 대문자(.capitalize)/길이 len(name)*공백도 1글자로 인식*
print(names)

