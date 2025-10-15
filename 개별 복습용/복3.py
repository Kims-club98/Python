# 다음 검색 하기

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

keyword=input('다음 검색어>')

browser=webdriver.Chrome()
browser.maximize_window()

url=f'https://search.daum.net/search?w=tot&DA=YZR&t__nil_searchbox=btn&q={keyword}'
browser.get(url)
time.sleep(2)

resert=browser.find_element(By.ID,'daumBtnSearch')
resert.
time.sleep(5)