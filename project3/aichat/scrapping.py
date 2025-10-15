import requests
from bs4 import BeautifulSoup
import time,re

#스크래핑 기본 세팅 함수
def creat_soup(url):
    res=requests.get(url)
    soup=BeautifulSoup(res.text,'lxml')
    return soup

#날씨
def weather(query):
    url=f'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query={query}'
    soup = creat_soup(url)
    temp = soup.find('div', attrs={'class':'temperature_text'})
    time.sleep(1)
    if temp:
        temp = temp.getText()
    else:
        temp = ''
    return temp

#환율
def exchange():
    url = 'https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&ssc=tab.nx.all&query=환율'
    soup = creat_soup(url)
    rate = soup.find('span', attrs={'class':re.compile('^spt_con')}).find('strong')
    if rate:
        rate = rate.getText()
    else:
        rate = ''
    return rate

#주식(stock)
def stock(query):
    url=f'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query={query}'
    soup = creat_soup(url)
    price = soup.find('div', attrs={'class':re.compile('^spt_con')}).find('strong')
    if price:
        price = price.getText()
    return price

#응답 인공지능
def answer(input_text):
    answer_text = ''
    if '안녕' in input_text:
        answer_text = '안녕하세요? 반갑습니다.'
    elif '날씨' in input_text:
        temp = weather(input_text)
        answer_text = '오늘의 ' + temp + '입니다.'
    elif '환율' in input_text:
        rate = exchange()
        answer_text = '1달러 환율은 ' + rate + '입니다.'
    elif '주식' in input_text:
        price = stock(input_text)
        answer_text = '1주는 ' + price + '원 입니다.'
    elif '고마워' in input_text:
        answer_text = '별말씀을요.'
    else:
        answer_text = '다시 한번 말씀해 주시겠어요?'
    return answer_text

# if __name__=='__main__':
#     text=answer('환율')
#     print(text)