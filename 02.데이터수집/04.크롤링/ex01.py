# 가상의 브라우저를 띄움(10초동안 유지시켜줌)
 #스크래핑: 정적인 자료를 가지고옴
 #크롤링: 버튼을 누르는 기능도 있음

from selenium import webdriver #브라우저
from selenium.webdriver.common.by import By
import time


brower = webdriver.Chrome()
brower.get('https://naver.com')
# time.sleep(3)

but=brower.find_element(By.CLASS_NAME, 'MyView-module__link_login___HpHMW') #find element: 찾는다
but.click()
brower.back()
brower.forward()
brower.refresh()
time.sleep(10)