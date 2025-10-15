#파이썬을 활용하여 API를 받아 연결하기

#네트워크 접속___
import requests
#화면 clear(도스 관련 명령어)
import os

#도서를 검색하는 함수___
def getBooks(url, query, page, size): #가져올 주소, 쿼리, 페이지, 규모
    try: #오류검증함수
        #"Authorization: KakaoAK ${REST_API_KEY}"
        headers={'Authorization':'KakaoAK 1ca6ee5e4daacc89499ce0270b956995'} #카카오 디벨로퍼의 API 키
        url=f'{url}&query={query}&page={page}&size={size}'
        res= requests.request(method='get',url=url, headers=headers)
        data=res.json()
        documents=data['documents']
        if len(documents)==0:
            print('검색된 도서가 없습니다.')
        
        for doc in enumerate: #documents 에서 doc를 뺌
            title=doc['title']
            price=doc['sale_price']
            authors=doc['authors'] #string[] 배열함수
            publisher=doc['publisher']
            print(title, price,','.join(authors), publisher) #배열의 함수(authors)를 ,로 연결하도록 바꾸는 함수 .join
            
    except Exception as err:
        print('접속오류!', err)

if __name__=='__main__':
    url="https://dapi.kakao.com/v3/search/book"
    page=1
    size=10
    os.system('cls')
    while True:
        qurey=input('검색도서명 >')
        if qurey=="":break
        getBooks(url,qurey,page,size)
