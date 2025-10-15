from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time, re

options=webdriver.ChromeOptions()
options.add_argument('headless')
browser=webdriver.Chrome(options=options)
browser.maximize_window()

url='https://www.weather.go.kr/w/index.do'
browser.get(url)

#전국 text
ei=browser.find_element(By.XPATH, '//a[text()="전국"]')
ei.click()
time.sleep(2)

#어제 xpath
xpath='//*[@id="content-body"]/div[4]/div/div/div[1]/ul/li[1]/a'
el=browser.find_element(By.XPATH, xpath)
el.click()
time.sleep(2)

#출력
soup=BeautifulSoup(browser.page_source, 'lxml')
local=soup.find('div',{'class':'minmax'})
els=local.find_all('dl',attrs={'class':re.compile('^po2_1')})
for idx,el in enumerate(els):
    name=el.dt.getText()
    tempR=el.find('span',{'class':'red'}).getText()
    tempB=el.find('span',{'class':'blue'}).getText()
    print(idx+1, name, tempR, tempB)