from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import os

options=webdriver.ChromeOptions()
options.add_experimental_option('detach',True)
browser=webdriver.Chrome(options=options)
browser.maximize_window()

keyword='파이썬'
url=f'https://www.hanbit.co.kr/search/search_list.html?keyword={keyword}'
browser.get(url)

#더보기
es=browser.find_element(By.XPATH, '//*[@id="container"]/div[1]/ul/li[3]/a')
es.click()
time.sleep(2)

soup=BeautifulSoup(browser.page_source, 'lxml')
books=soup.find('div',{'class':'ser_list_wrap'}).find_all('li',{'class':'ser_bg'})

book_list=[] #딕서너리 키: 값 ...
for book in books:
    no=len(book_list) + 1
    title=book.strong.getText()
    image=book.img['src']
    autor=book.span.getText()
    link='https:' + book.a['href']
    print(title,image,autor,link)

    data={'no':no, 'title':title, 'image':image, 'autor':autor, 'link':link}
    book_list.append(data)

# json파일에 저장
import json

os.makedirs('data', exist_ok=True)


with open('data/books.json','w',encoding='utf-8') as file:
    json.dump(list, file, indent='\t', ensure_ascii=False)


print('프로그램을 종료합니다!')



