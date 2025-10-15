import requests
from bs4 import BeautifulSoup

def weather(city):
    city=city+'날씨'
    url=f'https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&ssc=tab.nx.all&query=%EC%84%9C%EC%9A%B8%EB%82%A0%EC%94%A8&oquery={city}&tqi=j7PKYsqo1e8ssB8wiIRssssstPZ-028575&ackey=4cdx4obg'
    res=requests.get(url)
    # print(res)
    soup=BeautifulSoup(res.text,'lxml')

    summary=soup.find('p',attrs={'class':'summary'}).getText()
    # print(summary)

    temp=soup.find('div',attrs={'class':'temperature_text'}).strong.contents[1] #[0] 현재온도 / [1]26.5 / [2] º(content[] 내용에서 몇번째를 불러올지?)
    # print(temp)

    lowest=soup.find('span',attrs={'class':'lowest'}).contents[1]
    # print(lowest)

    highest=soup.find('span',attrs={'class':'highest'}).contents[1].replace('°','') # .get_text(): 최고기온 33도씨(기호) / .content[1] 33도씨(기호)
    # print(highest)

    print('[오늘의 날씨]')
    print('-'*50)
    print({summary})
    print(f'현재온도:{temp} (최저: {lowest}도 | 최고: {highest})도)')
    print('-'*50)
    
if __name__=='__main__':
        while True:
            city=input('지역명>')
            if city=='':break
            weather(city)