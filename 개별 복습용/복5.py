from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import requests
options=webdriver.ChromeOptions()
options.add_experimental_option('detach',True)
browser=webdriver.Chrome(options=options)

url='https://flight.naver.com/'
browser.get(url)
time.sleep(2)



res=requests(url)
soup=BeautifulSoup()

browser.maximize_window()

bt=browser.find_element('button',{'class':'FullscreenPopup_close'})
bt.click()
time.sleep(3)