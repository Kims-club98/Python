from fuction import menuPrint, inputNum, grade #외부에서 함수를 사용 시 가장 최상단에 선언을 해줘야 사용이 가능함 # function에서 menuPrint inputNum grade를 찾아옴

scores =[
    {'name':'홍길동', 'kor':90, 'eng':80, 'mat': 70},
    {'name':'이순신', 'kor':95, 'eng':90, 'mat': 80},
] # dict 목록을 score (score(name) 식으로 사용 가능)

def search(name):
    isfind = False #찾기 전 False
    for index, s in enumerate(scores): #찾기 시작
        if s['name'].find(name) != -1: # list의 name과 find 해야 하는 name이 일치 (!= -1 틀리지 않았을 때)
            isfind = True
            tot = s['kor'] + s['eng'] + s['mat']
            avg = tot/3
            print(index, s['name'], s['kor'], s['eng'], s['mat'], f'{avg:.2f},', grade(avg))
    if isfind == False: # is not isfind도 가능 
        print('검색 결과가 없습니다.')
    
while True:
    menuPrint('성적관리')
    menu = input('메뉴선택>')
    if menu =='0':
        print('프로그램을 종료합니다.')
        break
    elif menu=='1': #입력
        name = input('이름>')
        kor = inputNum('국어')
        eng = inputNum('영어')
        mat = inputNum('수학')
        scores.append({'name':name, 'kor':kor, 'eng':eng, 'mat':mat}) # 입력했던 name, kor, eng, mat를 list에 추가해줌
        print('입력성공') #append 가 잘 될 경우 성공 표시가 됨
    
    elif menu =='2': #검색 (이름을 입력받으면 검색됨)
        search_name = input('검색이름>') #부분일치하여도 데이터를 추출해줌
        search(search_name)


    elif menu == '3': #목록 입력
        if len(scores)==0:
            print('등록된 데이터가 없습니다.')
            continue #계속 진행됨
        search('')
        for s in scores:
            tot = s['kor'] + s['eng'] + s['mat']
            avg = tot/3
            print(s['name'], s['kor'], s['eng'], s['mat'], f'{avg:.2f},', grade(avg))
    
    elif menu =='4': #삭제 pop(인덱스 번호로 삭제, 이순신 0 심청이 1)
        del_name = input('삭제이름>')
        search(del_name)
        if isfind == True:
            index = inputNum('삭제번호>')
            scores.pop(index)
            print('삭제완료!')

        isfind = False # isfind = 찾은 경우는 True / 찾지 못한 것 = False
        for index, s in enumerate(scores): #인덱스에서 scores의 enumerate 함수를 이용
            if s['name'].find(del_name) != -1: # -1이 != : 찾았다
                print(index, s['name'])
                isfind = True # if isfind: 도 동일함
            if isfind:
                index = inputNum('삭제번호>')
                scores.pop(index)

    elif menu == '5': #수정
        edit_name = input("수정이름>")
        search(edit_name)

        if isfind ==True:
            index = inputNum("수정번호")
            s = scores[index] #기존 내용을 가져와서 보면서 수정하도록 함

            name = input(f"수정이름:{s['name']}>")
            if name != "": s['name']=name

            kor = inputNum(f"국어: {s['kor']}>")
            if kor != 0: s['kor'] = kor

            eng = inputNum(f"영어: {s['eng']}>")
            if eng != 0:  s['eng'] = eng

            mat = inputNum(f"수학: {s['mat']}>")
            if mat != 0: s['mat'] = mat
            scores[index] =s

    else:
        print('삭제할 이름이 없습니다.')
                
