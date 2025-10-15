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

soup=BeautifulSoup(browser.page_source,'lxml')

store=browser.find_element(By.ID,'storeListUL')
lis=store.find_elements(By.TAG_NAME,'li')
lis=[li.get_attribute('data-no') for li in lis]
print(lis)