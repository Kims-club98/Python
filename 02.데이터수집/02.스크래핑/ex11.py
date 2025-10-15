import requests
from bs4 import BeautifulSoup

def creat_soup(url):
    res=requests.get(url)
    soup=BeautifulSoup(res.text,'lxml')
    return soup

# 제목, 기사주소
def scrap(section):
    url=f'https://news.naver.com/section/{section}'
    soup=creat_soup(url)
    news=soup.find('ul', attrs={'class':'sa_list'})
    li=news.find_all('li',limit=5)
    if li ==0: print('기사를 찾을 수 없습니다')
    for idx, item in enumerate(li):
        title=item.find('strong',attrs={'class':'sa_text_strong'}).getText()
        # print(idx+1, title)
        link=item.find('a')['href']
        # print(link)
        print(f"{idx+1}. {title}")
        print(f"   링크: {link}")


if __name__=='__main__':
    while True:
        section = input('경제:101 |사회 102 | 생활º문화 103 | ITº과학 104 |세계 105 > >')
        if section=='': 
            print('101~105중에서 선택하세요')
            break
        scrap(section)

