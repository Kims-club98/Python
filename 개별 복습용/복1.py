# google 검색 페이지를 html로 저장하기(이번에는 네이버)
import os
import requests

path=f'{os.getcwd()}/data'
if not os.path.exists(path):
    os.makedirs(path)

print('네이버 이미지 검색하기')
name=input('이름>')
url=f'https://search.naver.com/search.naver?ssc=tab.image.all&where=image&sm=tab_jum&query={name}'
res=requests.get(url)

file_name=f'data/{name}.html'
with open(file_name,'w',encoding='utf-8-sig') as file:
    file.write(res.text)