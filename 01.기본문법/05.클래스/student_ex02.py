from student import Student

studnets = [    
    {'no':'01', 'name':'홍길동', 'dept':'전자과', 'birthday':'00-10-04'},
    {'no':'02', 'name':'심청이', 'dept':'전기과', 'birthday':'02-12-17'},
] #리스트 생성

while True:    
    print('--------------------------')
    print('|1.등록|2.목록|3.삭제|0.종료')
    print('--------------------------')
    menu = input('메뉴선택>')
    if menu == "0": 
        break

    elif menu == "1": #등록 
        s = Student()
        s.no = input('번호>')
        s.name = input('이름>')
        studnets.append(s.info()) #info 함수를 append함 / s.info는 dictionary를 append
        
    elif menu == "2": #목록
        for s in studnets: # for문에서 student를 꺼냄
            stu = Student()
            stu.no = s['no']
            stu.name =s['name']
            stu.dept=s['dept']
            stu.birthday=s['birthday']
            stu.info_print()
    
    elif menu == "3": #삭제
        no = input('삭제번호>') 
        for idx, s in enumerate(studnets): # 중요 idx 
            if no==s['no']:
                studnets.pop(idx)
                print('삭제완료!')
                break
