import requests
from bs4 import BeautifulSoup
import csv

file_name='data/할리스매장.csv'
file=open(file_name,'w',encoding='utf-8-sig',newline="")
writer=csv.writer(file)
title=['NO','지역명','매장명','주소','전화번호']
writer.writerow(title)

for page in range(1,10):
    url=f'https://www.hollys.co.kr/store/korea/korStore2.do?pageNo={page}&sido=%EC%84%9C%EC%9A%B8&gugun=&store='
    res=requests.get(url)
    soup=BeautifulSoup(res.text,'lxml')


    table=soup.find('table',attrs={'class':'tb_store'})
    rows=table.find_all('tr')
    for idx, row in enumerate(rows):
        if idx==0: continue
        cols=row.find_all('td')
        region=cols[0].getText().strip()
        name=cols[1].getText().strip()
        address=cols[3].getText().replace(',',' ').replace('.',' ').strip()
        phone=cols[5].getText().replace('.',' ').strip()
        data=[idx, region, name, address, phone]
        writer.writerow(data)
    