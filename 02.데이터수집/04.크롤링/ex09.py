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

# 전국
xpath='//*[@id="content-body"]/div[4]/h2/a'
e=browser.find_element(By.XPATH, xpath)
e.click()
time.sleep(2)

#예보
xpath='//*[@id="content-body"]/div[4]/div/div/div[1]/ul/li[3]'
a=browser.find_element(By.XPATH, xpath)
a.click()
time.sleep(2)

#요일반복선택
for i in range(1,8):
    xpath=f'//*[@id="local-weather"]/div/div[{i}]/h3/a'
    el=browser.find_element(By.XPATH, xpath)
    el_clean=el.text.replace("\n","")
    print(f'____________________{el_clean}_____________________')

    soup=BeautifulSoup(browser.page_source,'lxml')
    local=soup.find('div',{'id':'weather'})
    es=local.find_all('dl',{'class':re.compile('^po_')})
    for idx, e in enumerate(es):
        area=e.find('dt').getText()
        temp=e.find('span').getText()
        weather=e.find('i').getText()
        
        print(idx+1, area, temp,'도', f'({weather})')