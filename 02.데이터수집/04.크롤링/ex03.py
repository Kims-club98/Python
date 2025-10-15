from selenium import webdriver

option=webdriver.ChromeOptions()
option.add_experimental_option('detach',True) #웹 브라우저가 항상 실행하기
brower=webdriver.Chrome(options=option)
brower.maximize_window() # 브라우저 창을 최대화로 열기

url='https://flight.naver.com' #url입력 시 http://로 해야 오류발생 X
brower.get(url)
brower.get_screenshot_as_file('data/flight.png')
brower.quit()