import pandas as pd
import os
from  ex05 import *

file_name='C:/Python/03.데이터분석/01시리즈/data/학생정보.csv'

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

while True:
    os.system('cls')
    info=pd.read_csv(file_name, index_col='지원번호')
    info.fillna('',inplace=True)
    cols=info.columns

    print('-'*55)
    print('〓'*11+ ' 학생정보 ' +'〓'*11)
    print('1.등록 | 2. 목록 | 3. 검색 | 4. 삭제 | 5. 수정 | 6. 성적관리 | 0.종료')
    print('-'*55)
    menu=input('메뉴선택>')
    if menu =='0':
        input('프로그램을 종료합니다!')
        break
    elif menu=='1': #등록
        new_no=info.index.max()+1
        print(f'지원번호>{new_no}')
        name=input('이름>')
        if name=="":
            continue
        school=input('학교명>')
        height=inputNum('키>')
        if height=='': height=0
        sw=input('SW특기>')
        info.loc[new_no]=[name, school, height, sw]
        sel=input('정말로 등록하시겠습니까?(Y)>')
        if sel=='Y' or sel=='y':
            info.to_csv(file_name)
            print('등록완료')
        input('아무키나 누르세요!')

    elif menu=='2':
        for idx in info.index:
            row=info.loc[idx]
            print(f"지원번호:{idx}",end=' ')
            for col in cols:
                print(f"{col}:{row[col]}",end=' ')
            print()
            print('-'*30)
        input('아무키나 누르세요!')

    elif menu=='3':
        while True:
            sel=input('1.이름|2.학교|3.SW특기>')
            if sel=='': break
            wd1=input('검색어>')
            if sel=='1': filt=info['이름'].str.contains(wd1)
            if sel=='':
                print('번호를 선택해주세요!')
                continue
            elif sel=='2': filt=info['학교'].str.contains(wd1)
            if sel=='':
                print('번호를 선택해주세요!')
                continue
            elif sel=='3': 
                word=wd1.upper()
                filt=info['SW특기'].str.upper().str.contains(wd1)
            idxs=info[filt].index
            if sel=='':
                print('번호를 선택해주세요!')
                continue
            if len(idxs)==0:
                print("해당 레이어에 데이터가 존재하지 않음")
            else:
                for idx in idxs:
                    row = info.loc[idx]
                    print(f'지원번호:{idx}',end=' ')
                    for col in cols:
                        print(f'{col}:{row[col]}')
                    print()
                    print('-'*50)    
        input('아무키나 누르세요')
    elif menu=='4': #삭제e,index=False)
        no=inputNum('지원번호>')
        if no in info.index:
            row=info.loc[no]
            for col in cols:
                print(f"{col}:{row[col]}")
            sel=input('삭제하실래요?(Y)>')
            if sel=='Y' or sel=='y':
                 info.drop(index=no, inplace=True)
                 info.to_csv(file_name)
                 input('삭제성공!')
    elif menu=='5':
        no=inputNum('지원번호>')
        if no in info.index:
            row=info.loc[no]
            name=input(f"이름:{row['이름']}>")
            if name=='': name=row['이름']
            school=input(f"학교명:{row['학교']}>")
            if school=='': school=row['학교']
            height=inputNum(f"키:{row['키']}>")
            if height=='': height=row['키']
            sw=input(f"SW특기:{row['SW특기']}>")
            if sw=='': sw=row['SW특기']
            sel = input('수정하실래요?(Y)>')
            if sel=='Y' or sel=='y':
                info.loc[no]=[name,school,height,sw]
                info.to_csv(file_name)
                input('수정완료!')    
        else:
            print('지원번호가 존재하지 안습니다!')
        input('아무키나 누르세요!')
    elif menu=='6':
        submenu()
    else:
        input('0에서 5사이를 입력하세요!')