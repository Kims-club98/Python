from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


options=webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
browser=webdriver.Chrome(options=options)
browser.maximize_window()
#_________________________________________________ 브라우저 옵션 삽입

def wait_until(xpath): 
    WebDriverWait(browser, 10).until(  #결과가 나오기까지 기다리는데 10초까지만 기다림
        EC.presence_of_all_elements_located((By.XPATH,xpath)))
    
#___________________________________결과가 나오기까지 기다리기

url='https://flight.naver.com/'
browser.get(url)
time.sleep(2)
#_________________________________브라우저 지정, 적용


btn=browser.find_element(By.CLASS_NAME,'FullscreenPopup_suspend') #elemant: 요소 1개 // elements 여러 요소
btn.click()
time.sleep(2)
#____________________________________ 7일간 보지 않기 버튼

el=browser.find_element(By.XPATH,'//button[text()="가는 날"]')
el.click()
time.sleep(2)

#_______________________________________가는날 선택(텍스트 값으로 선택하기)

els=browser.find_elements(By.XPATH,'//b[text()="25"]')
els[0].click()
time.sleep(2)

#________________________________________ 이번 달 25일 선택(여러 항목)

eld=browser.find_elements(By.XPATH,'//b[text()="26"]')
eld[0].click()
time.sleep(2)
#________________________________________ 이번 달 26일 선택

ed=browser.find_element(By.XPATH, '//b[text()="도착"]')
ed.click()
time.sleep(2)
#_______________________________________ 도착누르기

jeju_el=browser.find_element(By.XPATH, '//button[text()="제주"]')
jeju_el.click()
time.sleep(2)

#_______________________제주 선택하기

el_click=browser.find_element(By.XPATH, '//span[text()="항공권 검색"]')
el_click.click()
time.sleep(2)

#_______________________항공권 검색 클릭
try:
    first= '//*[@id="__next"]/div/main/div[4]/div/div[2]/div[2]/div[1]' #d이 내역은 copy-xpath로 찾음
    # wait_until(el.text)
    time.sleep(15)
    els=browser.find_elements(By.CLASS_NAME, 'domestic_Flight__8bR_b')
    for idx, el in enumerate(els):
        print(f'[{idx}],{el.text}')
        print('+'*50)
        
except:
    pass
finally:
    browser.quit()
    print('프로그램 종료')
#____________________________________________첫번째 내역 출력
