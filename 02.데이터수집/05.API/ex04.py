import requests
import os

def getData(query):#api 키
    url=f"https://dapi.kakao.com/v2/local/search/address.json?query={query}"
    headers={'Authorization':'KakaoAK e779cdef1331864a0977eaff9b2fed22'} #카카오 디벨로퍼의 API 키
    res=requests.get(url, headers=headers)
    data=res.json()['documents']
    print(data)
    return data

if __name__=='__main__':
    os.system('cls')
    print()
    while True:
        query= input('검색어>')
        data=getData(query)
        if data=="":
            print('검색 내용이 없습니다.')
            continue
        for item in data:
            name=item['place_name']
            address=item['address_name']
            phone=['phone']
            print(name, address, phone)
        