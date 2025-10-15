#네이버에 자동 아이디/비번 입력
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

brower=webdriver.Chrome()
brower.get('https://naver.com')
btu=brower.find_element(By.CLASS_NAME, 'MyView-module__link_login___HpHMW')
btu.click()
time.sleep(2)

id=brower.find_element(By.ID,'id')
id.send_keys('naxen5611')
pw=brower.find_element(By.ID,'pw')
pw.send_keys('navernaver5611')
time.sleep(2)

login=brower.find_element(By.ID,'log.login')
login.click()
time.sleep(100)