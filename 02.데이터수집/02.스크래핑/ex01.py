import requests
from bs4 import BeautifulSoup

url='https://www.naver.com/'
res=requests.get(url)

soup=BeautifulSoup(res.text, 'lxml')
title=soup.title

print(1, title) #1=3 결과 같음
print(2, title.get_text())
print(3, soup.find('title'))

a=soup.a
print(4, a)

span=a.span
print(5,span)
print(6, span.getText())

attrs=a.attrs
print(7, a.attrs, type(attrs))

href=a['href']
print(8,href)

items=soup.find_all('a')
for item in items:
    print(9, item.span.get_text())
