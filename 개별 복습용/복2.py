import requests
from bs4 import BeautifulSoup
import csv
import re
headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36'}
url='https://finance.yahoo.com/markets/'
res=requests.get(url,headers=headers)
soup=BeautifulSoup(res.text,'lxml')

table=soup.find('table',attrs={'class':'world-indices'})
rows=table.find_all('tr')

for row in rows:
    cols=row.find_all('td')
    if len(cols) <=1:continue
    print(cols)

   
#___________________
import requests
from bs4 import BeautifulSoup

url='https://finance.naver.com/'
res = requests.get(url)
soup = BeautifulSoup(res.text, 'lxml')

#[Top종목]-[거래상위]
tbody = soup.find('tbody', attrs={'id':'_topItems1'})
trs = tbody.find_all('tr')

list = []
for idx, tr in enumerate(trs):
    up_down = tr['class']
    name = tr.a.getText()
    tds = tr.find_all('td')
    price = tds[0].getText()
    up_down_price=tds[1].getText().replace('하락','').replace('상승','').strip()
    #print(idx+1, name, price, up_down[0], up_down_price)
    list.append(f'{idx+1},{name},{price},{up_down[0]},{up_down_price}')
print(list)

file_name = 'data/거래상위.txt'
with open(file_name, 'w', encoding='utf-8') as file:
    for line in list:
        file.write(line + '\n')