from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def browser_ex():
    options=webdriver.ChromeOptions()
    options.add_experimental_option('detach',False)
    browser=webdriver.Chrome(options=options)
    url='https://land.naver.com/'
    browser.get(url)

    a=browser.find_element(By.CLASS_NAME,{'class':'queryInputHeader'})
    a.send_keys('청라자이')
    a.send_keys(Keys.ENTER)
    
import requests
from bs4 import BeautifulSoup
time.sleep(3)

browser=browser_ex()
soup=BeautifulSoup(browser.page_source, 'lxml')

es=soup.find_all('div',{'class':'item_list item_list--search'})

for idx, e in enumerate(es):
    print(f'---정보 {idx+1}---')
    title=e.find('div',{'class':'title'}).getText()
    address=e.find('div',{'class':'address'}).getText()
    type=e.find('strong',{'class':'type'}).getText()
    inf=e.find('span',{'class':'spec'}).getText()
    
    print(title)
    print(address)
    print(type + '|' + inf)

browser_ex()