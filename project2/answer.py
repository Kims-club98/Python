#크롤링(날씨,환율,주가) 하여 정보를 가지고 오고 aiSpeaker.py는 이를 받아서 tts로 변경해줌
import requests
import time
from bs4 import BeautifulSoup

# 1-1. 날씨 스크래핑 세팅
def creat_soup(url):
    res=requests.get(url)
    soup=BeautifulSoup(res.text,'html.parser') # lxml은 따로 install lxml을 해야 하며, 라이브러리 설치 불가할떄 html.'parser을 넣음
    return soup

# 1-2. 오늘 날씨
def weather(query):
    url=f'https://m.search.naver.com/search.naver?sm=mtp_hty.top&where=m&query={query}&ackey=oe9qpm0h'
    soup=creat_soup(url)
    temp=soup.find('div', attrs={'class':'temperature_text'}).find('strong')
    #temp 성공 시 가져오고, 실패 시 ''(공백) 출력
    if temp:
        temp=temp.getText()
    else:
        temp=''
    return temp


# 2. 환율 
def exchage():
    url='https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&ssc=tab.nx.all&query=%ED%99%98%EC%9C%A8&oquery=%ED%8C%8C%ED%8C%8C%EA%B3%A0&tqi=jMxpyspzL8wssCINXAwssssstPR-076018&ackey=f3aykt1x'
    soup=creat_soup(url)
    rate=soup.find('span',attrs={'class':'spt_con dw'}).find('strong')
    if rate:
        rate=rate.getText()
    else:
        rate=''
    return rate


# 3. 주식
def stock(query):
    url=f'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query={query}&ackey=cfg2y1a9'
    soup=creat_soup(url)
    price=soup.find('div',attrs={'class':'spt_con dw'}).find('strong')
    if price:
        price=price.getText()
    else:
        price=''
    return price

#테스트 목적 함수
if __name__=='__main__':
    temp=weather('광명날씨')
    rate=exchage()
    # price=stock('삼성주식')
    # print(price)
    print(temp)