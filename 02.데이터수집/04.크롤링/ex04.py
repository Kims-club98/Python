from selenium import webdriver
import os

os.makedirs('data', exist_ok=True)

option=webdriver.ChromeOptions()
option.add_argument('headless')
option.add_argument('widow-size=1920x1080')

brower=webdriver.Chrome(options=option)
url='https://flight.naver.com'
brower.get(url)

brower.get_screenshot_as_file('data/flight1980.png')
brower.quit()