# 해커스 오늘의 영어회화 출력(스크랩트)

import requests
from bs4 import BeautifulSoup
import re

def creat_soup(url): # 선언
    res=requests(url)
    res.raise_for_status()
    soup=BeautifulSoup(res.text,'lxml')
    return soup

def scrap_english():
    print('[오늘의 토익 문제]')
    url='https://www.hackers.co.kr/?c=s_lec/lec_study/mail_history&keywd=haceng_main_mailhistory&logger_kw=haceng_main_mailhistory'
    soup=creat_soup(url)

    sentences=soup.find_all('div',attrs={'id':re.complie('conv_txt')})