# 할리스 서울지역 매장점포현황(hollys.json파일 활용)으로 위도 경도값을 구함
import requests
import json
import os


#할리스 매장 주소 가져옴, 이름, 전화번호부, 휴대폰 번호를 출력'
def getAddress():
    with open('data/hollys.json','r',encoding='utf-8') as file:
        address=json.load(file)
        list=[]
        for add in address:
            data={'name': add['name'], 'address': add['address'], 'phone':add['phone']}
            list.append(data)
        return list

# 할리스 매장 정보(매장명, 주소, 전화번호)
def getXY(query): #쿼리값을 받아 위도 경도값을 얻는 함수
    url=f"https://dapi.kakao.com/v2/local/search/address.json?query={query}"
    headers={'Authorization':'KakaoAK e779cdef1331864a0977eaff9b2fed22'}
    res=requests.request(method='get',url=url,headers=headers)
    data=res.json()
    documents=data['documents']
    x=documents[0]['x']
    y=documents[0]['y']
    print(x,y) # 전북 삼성ㄷㅇ 100에 대한 위도 경도값
    return x, y


# def getAddress2(address):
#     print(address).split('')[:4]
#     address=' '.join(address)
#     print(address)
    

if __name__=='__main__':
    list=getAddress()
    list_json=[]
    for add in list:
        name=add['name']
        phone=add['phone']
        address=add['address']
        address= address.split(' ')[:4]
        address=' '.join(address)
        xy=getXY(address)
        x=xy[0]
        y=xy[1]
        # print(address, x, y, name, phone)
        data={'name':name, 'phone':phone, 'address':address, 'x':x, 'y':y}
        list_json.append(data)

    with open('data/hollys.json', 'w', encoding='utf-8') as file:
        json.dump(list_json, file, indent='\t', ensure_ascii=False)