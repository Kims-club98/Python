import requests
from bs4 import BeautifulSoup

url='https://comic.naver.com/index'
res=requests.get(url)

soup=BeautifulSoup(res.text, 'lxml')
title=soup.title

print(1,title)
print(2, title.get_text())
print(3, soup.find('title'))

a=soup.a
print(4,a)

span=a.span
print(5,span)