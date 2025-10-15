from selenium import webdriver
from selenium.webdriver.common.by import By 
from bs4 import BeautifulSoup
import time


options=webdriver.ChromeOptions()
options.add_experimental_option('detach',True)
browser=webdriver.Chrome(options=options)
browser.maximize_window()

url='https://www.coffeebeankorea.com/store/store.asp'
browser.get(url)

soup=BeautifulSoup(browser.page_source,'lxml')
ul=soup.find('ul',{'id':'storeListUL'})
stores=ul.find_all('li')
time.sleep(2)

list=[]
for store in stores:
    name=store.find('p',{'class':'name'}).find('span').contents[0]#여러개의 경우 contant로 가져옴 #세밀하게 가져올 경우 검사 내 span도 넣어줌
    address=store.find('p',{'class':'address'}).getText().strip()
    tel=store.find('p',{'class':'tel'}).getText().strip()
    print(name)
    print(address)
    print(tel)
    list.append([name,address,tel])

import csv
file=open('C:/Python/03.데이터분석/03커피빈/커피빈매장.csv','w', encoding='utf-8-sig',newline='')
writer=csv.writer(file)
writer.writerow({'Name','Address','Tel'})
writer.writerows(list)