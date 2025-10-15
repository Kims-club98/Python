import requests

def getData(query):
    url=f"https://dapi.kakao.com/v2/search/image?query={query}&size=20"
    headers={'Authorization':'KakaoAK e779cdef1331864a0977eaff9b2fed22'}
    res=requests.get(url,headers=headers)
    data=res.json()['documents']
    return data

if __name__=='__main__':
    query='seoul'
    list=getData(query)
    for item in list:
        img_url=item['image_url']
        res=requests.get(img_url) #이미지 url 가져오기/접속하기
        if res.status_code==200:
            print(img_url, res.status_code)
            index=img_url.rindex('/')
            file_name=img_url[index+1:]
            print(file_name)
            #파일 다운로드
            with open(f'data/image/{file_name}','wb') as file:
                file.write(res.content)



