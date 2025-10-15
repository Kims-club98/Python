import pandas as pd
import os
file_score='C:/Python/03.데이터분석/01시리즈/data/학생성적.csv'
file_info='C:/Python/03.데이터분석/01시리즈/data/학생정보.csv'

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

def submenu():
    while True:
        score= pd.read_csv(file_score, index_col='지원번호')
        info= pd.read_csv(file_info, index_col='지원번호')
        df=info.join(score)
        df['총점']=df.apply(lambda x: sum(x['국어':'사회']),axis=1)
        df['평균']=df['총점']/5
        df.fillna(0,inplace=True)
        cols=['국어','영어','수학','과학','사회']
        os.system('cls')
        print('-'*55)
        print('〓'*11+ ' 학생정보 ' +'〓'*11)
        print('1.등록 | 2. 목록 | 3. 검색 | 4. 삭제 | 5. 수정 | 0.종료')
        print('-'*55)
        menu=input('메뉴선택>')
        if menu =='0':
            input('프로그램을 종료합니다!')

        elif menu=='1':
            no=inputNum('지원번호>')
            if not no in info.index:
                print('등록되지 않은 지원번호입니다.')
            elif no in score.index:
                print('이미 성적이 등록된 지원번호입니다.')
            else:
                row=info.loc[no]
                print(f"이름:{row['이름']}")
                grade=[]
                for col in cols:
                    num=inputNum(f"{col}>") #col이 국어/수학...
                    if num=="": 
                        num=0
                        grade.append()
                score[no] = grade
                score.to_csv(file_score)
                print('등록완료!')

            input('아무키나 누르세요!')
        elif menu=='2': # 목록구성
            while True:
                sel=inputNum('1.최신입력순|2.이름순|3.성적순')
                if sel=='':break
                if sel==1: df=df.sort_index(ascending=True)
                elif sel==2:df=df.sort_values('이름')
                elif sel==3:df=df.sort_values('평균',ascending=False)
                for idx in df.head().index:
                    row=df.loc[idx] #df의 인덱스를 하나씩 가지고 옴
                    print(f"지원번호:{idx:02d}", end=' ') 
                    print(f"이름:{row['이름']}",end=' ') #이름의 위치 row
                    print(f"학교:{row['학교']}", end=' ')
                    for col in cols: #국영수과사 가지고 옴
                        print(f"{col}:{row[col]:.0f}",end=' ')
                    print(f"평균:{row['평균']}:.2f")
                    print()
                    print('-'*50)
                input('아무키나 누르세요!')

        elif menu=='3': #검색
            while True:
                sel=inputNum('1.지원번호|2.학교|3.이름>')
                if sel=='':
                    break
                elif sel==1: #inputnum은 정수 So '1'로은 인식을 못함
                    no=inputNum('지원번호>')
                    if not no in df.index:
                        print('해당 지원번호는 없습니다.')
                    else:
                        row=df.loc[no]
                        print(f"지원번호:{idx},이름:{row['이름']},학교:{row['학교']},평균:{row['평균']:.2f}")
                elif sel==2:
                    word=input('학교명>')
                    filt=df['학교'].str.contains(word)
                    if len(df[filt].index)==0:
                        print('검색내용이 없습니다.')
                        continue
                    for idx in df[filt].index:
                        row=df.loc[idx]
                        print(f"지원번호:{idx},이름:{row['이름']},학교:{row['학교']},평균:{row['평균']:.2f}")
                elif sel==3:
                    word=input('이름>')
                    filt=df['이름'].str.contains(word)
                    if len(df[filt].index)==0:
                        print('검색된 내용이 없습니다.')
                        break
                    for idx in df[filt].index:
                        row=df.loc[idx]
                        print(f"지원번호:{idx},이름:{row['이름']},학교:{row['학교']},평균:{row['평균']:.2f}")
            input('아무키나 누르세요!')
        elif menu=='4': #삭제
            no=inputNum('지원정보>')
            if not no in info.index:
                print('등록된 지원번호가 없습니다.')
            elif not no in score.index:
                print('등록된 성적이 없습니다.')
            else:
                row=df.loc[no]
                print(f"이름:{row['이름']}")
                for col in cols:
                    print(f"{col}:{row[col]}")
                sel=input('삭제하실래요?(Y)>')
                if sel =='Y' or sel =='y':
                    score.drop(index=no,inplace=True)
                    score.to_csv(file_score)
                    input('삭제완료!')

        elif menu=='5': # 수정
            no=inputNum('지원번호>')
            if not no in info.index:
                print('등록된 지원번호가 없습니다.')
            elif not no in score.index:
                print('등록된 성적이 없습니다.')
            else:
                row=df.loc[no]
                print(f"이름:{info.loc[no,'이름']}")
                grade=[]
                for col in cols:
                    num=inputNum(f"{col}:{row[col]}>")
                    if num=='': num=0
                    grade.append(num)
                sel=input('정말로 수정하실래요?>')
                if sel=='Y'or sel=='y':
                    score.loc[num]=grade
                    score.to_csv(file_score)
                    print('수정완료!')

            input('아무키나 누르세요!')
        elif menu=='0':
            input('아무키나 누르세요!')
        else:
            input('0과 5사이를 입력하시오.')

# if __name__=='__main__':
#     submenu()