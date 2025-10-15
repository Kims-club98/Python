import requests
import csv #엑셀 함수 형태로 만듦
from bs4 import BeautifulSoup
import re

file_name='data/코스닥 거래 상위1-100.csv' #csv 파일 생성 후 저장
file=open(file_name, 'w',encoding='utf-8-sig', newline="")
writer=csv.writer(file)

# [top종목] - [거래상위] - [더보기] - [코스닥] -목표: 100위까지 스크랩
url='https://finance.naver.com/sise/sise_quant.naver?sosok=1'
res=requests.get(url) #정보 res로
soup=BeautifulSoup(res.text,'lxml') #soup에 결과 이동

table=soup.find('table',attrs={'class':'type_2'})
rows=table.find_all('tr')

data=[]
for row in rows:
    cols=row.find_all('td')
    if len(cols) <=1: continue
    data=[re.sub('\t|\n|하락|상승|보합','', col.getText()) for col in cols] #re.sub()식에서 |가 or에 해당됨
    writer.writerow(data)
    

