import requests
from bs4 import BeautifulSoup

url='https://finance.naver.com/'
res=requests.get(url)

soup=BeautifulSoup(res.text,'lxml' )

top5= soup.find('div', attrs={'class':'aside_area aside_popular'})
items=top5.find_all('a')
print(len(items))

for item in items:
    text=item.get_text()
    title=item.get_text()

    print(title)

text=item.find_all('tr')
t_price=text[0].get_text()
t_updonw=text[1].get_text()
print(title, t_price, t_updonw)

# 1 개 find
# 여러개 find_all
