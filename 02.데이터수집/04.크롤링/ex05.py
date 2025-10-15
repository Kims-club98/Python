# [쿠팡]-[검색어]-[노트북] 1페이지 결과의 상품 이름, 상품가격
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

option=webdriver.ChromeOptions()
option.add_experimental_option('detach',True) # 항상 브라우저가 열려있음
option.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36')
browser=webdriver.Chrome(options=option)
browser.maximize_window()
keyword='노트북'

# with open('data/gmarket.html','w',encoding='utf-8') as file:
#     file.write(browser.page_source)

url=f'https://www.gmarket.co.kr/n/search?keyword={keyword}'
browser.get(url)
time.sleep(2)

browser.execute_script('window.scrollTo(0,document.body.scrollHeight)') #웹의 스크롤을 맨 아래로 내려줌
time.sleep(5)

#____________________________스크래핑
from bs4 import BeautifulSoup
import re  
import json

soup=BeautifulSoup(browser.page_source,'lxml')
items=soup.find_all('div',attrs={'class':'box__item-container'})
cnt=0
list=[]
# print(len(items))
for idx,item in enumerate(items):
    title=item.find('span',{'class':'text__item'}).getText()
    price=item.find('strong',{'class':'text__value'}).getText()
    img='https:' + item.find('img',{'class':'image__item'})['src']
    pay_count=item.find('li',{'class':re.compile('list-item__pay-count$')})
    link=item.a['href']
    if pay_count:
        pay_count=re.sub('구매|건|,','',pay_count.getText()).strip()
        pay_count=int(pay_count)
    else:
        pay_count=0

    if pay_count >=100:
        cnt +=1
        print(idx+1,title,img,f'구매건수:{pay_count}')
        data={'no':cnt, 'title':title, 'price':price, 'count':pay_count, 'img':img, 'link':link}
        list.append(data)

#_____________________________________ json 파일에 dump
with open('data/gm.json','w',encoding='utf-8') as file:
    json.dump(list, file, indent='\t', ensure_ascii=False)

browser.quit()
print('프로그램종료')

# query=browser.find_element(By.NAME,'q')
# time.sleep(2)
# query.send_keys('노트북')
# query.send_keys(Keys.ENTER)

# search_button=browser.find_element(By.CLASS_NAME, 'select')
# search_button.click()
# time.sleep(2)
