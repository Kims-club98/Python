import os, pandas as pd

file_pro='data/교수.csv'

def pro_list():
    pro=pd.read_csv(file_pro, index_col='교수번호')
    for idx, row in pro.iterrows(): #하나씩 하나씩 가지고 옴
        print(idx, row['교수이름'], row['교수학과'], row['임용일'], end='')
        print( f"{row['급여']:,} {row['교수직급']}")


while True:
    os.system('cls')
    print('-'*50)
    print('***** 학사관리 *****')
    print('-'*50)
    print('[1] 교수목록')
    print('[2] 교수검색')
    print('[3] 학생목록')
    print('[4] 학생검색')
    print('[5] 강좌목록')
    print('[6] 강좌검색')
    print('-'*50)
    
    menu=input('메뉴선택>')
    if menu =='1': #교수목록
        pro_list()
        input('아무키나 입력하세요!')


    elif menu =='2':
        pass
    elif menu =='3':
        pass
    elif menu =='4':
        pass
    elif menu =='5':
        pass
    elif menu =='6':
        pass
    else:
        pass