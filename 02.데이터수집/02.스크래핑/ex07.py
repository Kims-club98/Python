# 이미지 불러오기
import requests # 가져오기
from bs4 import BeautifulSoup #분석
import os

path=os.getcwd() + '/data/books'
if not os.path.exists(path):
    os.mkdir(path)


url='https://www.hanbit.co.kr/store/store_submain.html'
res=requests.get(url)
soup=BeautifulSoup(res.text,'lxml')

section=soup.find('ul',attrs={'id':'new_books_slider'})
imgs=section.find_all('img')
for idx,img in enumerate(imgs):
    #print(f"book{idx:02d}.jpg", img['src'])
    url=img['src']
    res_img=requests.get(url)
    file_name=path + f'/book{idx:02d}.jpg'
    with open(file_name, 'wb') as file:
        file.write(res_img.content)

