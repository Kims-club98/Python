#전국 날씨 추출하기(기상청)
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
from bs4 import BeautifulSoup
import re, time
import datetime #현재 날짜를 가지고 올 수 있음

date=time.strftime(f'%Y년 %M월 %D일 %H시 : %M분')

options=webdriver.ChromeOptions()
# options.add_experimental_option('detach',True) # 열기 O 시
options.add_argument('headless')
broswer=webdriver.Chrome(options=options)
broswer.maximize_window()
#____________________________________________________ 크롤링 기본 세팅

url='https://www.weather.go.kr/w/index.do'
broswer.get(url)

soup=BeautifulSoup(broswer.page_source, 'lxml') # 텍스트만: res.txt, 'lxml'
local=soup.find('div',{'id':'weather2'})
#print(local)

els=local.find_all('dl',{'class':re.compile('^po_')})
# print(len(els))

print(date)
for el in els: #각 요소별로 가져오기
    name=el.dt.getText()
    temp=el.span.getText()
    weather=el.i.getText()
    print(name, temp, weather)
    print('+'*30)

