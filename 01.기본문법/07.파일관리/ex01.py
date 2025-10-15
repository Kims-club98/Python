import os
path = os.getcwd() #.getcwd() : 현재 작업중인 폴더의 위치 추출
print('작업폴더:', path)



#주소 데이터를 파일에 저장하기
with open('data/juso.txt','a',encoding='utf-8')as file: #a= 1개 txt에 한번에 넣음 / w는 초기화하여 자료를 넣어줌
    name = '홍길동'
    phone = '010-1010-1010'
    adress = '서울특별시 강서구 화곡동'
    file.write(f'{name},{phone},{adress}\n')

    name = '심청이'
    phone = '010-1010-2010'
    adress = '서울특별시 노원구 중계동'
    file.write(f'{name},{phone},{adress}\n')
