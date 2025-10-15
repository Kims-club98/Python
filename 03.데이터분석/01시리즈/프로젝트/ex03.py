import pandas as pd
import os
file_name='data/학생성적.csv'
score=pd.read_csv('data/학생성적.csv')
cols=score.columns # 열 라인

def inputNum(title):
    while True:
        num=input(title)
        if num=="":
            return ''
        elif not num.isnumeric():
            print('점수는 숫자로 입력하세요!')
            continue
        else:
            return int(num)

#
def sort_list():
    while True:
        for idx, col in enumerate(cols):
            print(f'{idx}:{col}',end='|')
        print()
        sel=inputNum('선택>')
        if sel=='': break
        score = score.sort_values(cols[sel], ascending=False)
        for idx in score.index:
            row=score.loc[idx]
            for col in cols:
                print(f'{col}:{row[col]}',end=',')
            print()


while True:
    os.system('cls')
    print('-'*55)
    print('〓'*11+ ' 성적관리 ' +'〓'*11)
    print('1.등록 | 2. 목록 | 3. 검색 | 4. 삭제 | 5. 수정 | 0.종료')
    print('-'*55)
    menu=input('메뉴선택>')
    if menu =='0':
        input('프로그램을 종료합니다!')
        break
    elif menu=='1':
        index=max(score.index)+1 #저장할 index 번호
        no=score['지원번호'].max()+1
        grade=[]
        for idx, col in enumerate(cols):
            if idx==0:
                print(f'지원번호>{no}')
            else:
                num=inputNum(f"{col}>")
                if num=='':
                    num=0
                grade.append(num)
        score.loc[index]=[no, grade[0], grade[1], grade[2], grade[3], grade[4]]
        score.to_csv(file_name, index=False)
        print('등록성공')
        print('아무키나 누르세요!')

    elif menu=='2':
        sort_list()
        input('아무키나 누르세요!')
    elif menu=='3':
        while True:
            no=inputNum('지원번호>')
            if no=='':
                break
            filt=score['지원번호']==int(no) #no가 3번이면 지원번호가 3번
            idxs=score[filt].index #idxs는 score의 filt조건에 만족하는 인덱스 값
            if len(idxs)==0:
                print('해당되는 지원번호가 없습니다!')
            else:
                row=score.loc[idxs[0]] #score의 idx값을 가지고 옴
                for col in cols:
                    print(f"{col}:{row[col]}",end=',')
            print()

    elif menu=='4': #삭제
         no=inputNum('지원번호>')
         filt=score['지원번호']==no
         idx=score[filt].index #idx는 배열
         if len(idx)==0:
             print('해당하는 지원번호가 없습니다.')
         else:
            row=score.loc[idx[0]]
            for col in cols:
                print(f"{col}:{row[col]}",end=',')
            print
            sel=input('삭제하시겠습니까?(Y)>')
            if sel=='Y' or sel=='y':
                score.drop(index=idx[0], inplace=True)
                score.to_csv(file_name,index=False)
                print('삭제완료!')  
         input('아무키나 누르세요!')
    elif menu=='5':
        no =inputNum('지원번호>')
        idx=score[score['지원번호']==no].index
        if len(idx)==0:
            print('해당 지원 번호가 없습니다!')
        else:
            row=score.loc[idx[0]]
            grade=[] #수정된 값을 넣을 리스트값
            for index, col in enumerate(cols): # return idx, col
                if index==0: continue
                num=inputNum(f"{col}:{row[col]}>")
                if num=='': 
                    num=row[col]
                grade.append(num)
            sel=input('수정하실래요?(Y)>')
            if sel=='Y' or sel=='y':
                score.loc[idx[0]]=[no, grade[0], grade[1], grade[2], grade[3], grade[4]] # 과목 수정된 값을 넣어줌
                score.to_csv(file_name, index=False)
                print('수정완료!')
    else:
        input('잘못 누르셨습니다.' 
        '0에서 5사이를 입력하세요!')