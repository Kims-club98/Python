from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time, re
import requests
import os

options=webdriver.ChromeOptions()
options.add_experimental_option('detach',True)
browser=webdriver.Chrome(options=options)
browser.maximize_window()

url='https://www.coffeebeankorea.com/store/store.asp'
browser.get(url)

browser.execute_script("storePop2('142')") #괄호 내에서는 Java script용 함수 사가능 (31항의 매장을 자세히 보기를 열어라)
time.sleep(5)

soup=BeautifulSoup(browser.page_source, 'lxml')

#매장이름찾기(soup.select로... / 기존 find)
name=soup.select('div.store_txt > h2')[0].string #div테이블 스토어 텍스트에 h2위치임 
info=soup.select('div.store_txt > table.store_table > tbody > tr > td')
address=info[2].getText() # get_text()
phone=info[3].string

print('매장명:',name)
print('매장주소:',address)
print('매장전화:',phone)

#사진 가져오기
imgs=soup.select('div.slick-slide > img')
for img in imgs:
    src='https://www.coffeebeankorea.com/' + img.attrs['src']
    print(src)
    index= src.rindex('/')
    file_name=src[index:]
    print(file_name)
# 웹에 접속/저장

path='data/store'
if not os.path.exists(path):
    os.mkdir(path)

with open(path + file_name, 'wb') as file:
    res=requests.get(src)
    file.write(res.content)