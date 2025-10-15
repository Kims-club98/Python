import json
import os
import folium #지도를 구성하는데 필요함

#1. json 파일 읽어오기(함수로 만들어오기)
def getAddress():
    with open('data/hollys_location.json','r',encoding='utf-8') as file:
        data=json.load(file)
        return data
    
# 주소를 통해 검색을 하기 위해 찾는 함수
def searchAdress(address): #list는 여러개의 dictionary로 이루어짐
    list = getAddress()
    search_list=[]
    for store in list:
        if store['address'].find(address) != -1:
            print(f"{store['name']}, {store['address']},{store['phone']}")
            search_list.append(store)

    return search_list # 검색한 내용을 hollys_location.json에서 찾은 후 그 결과를 search_list에 넣어주고 return해줌

# 지도를 만들어 주는 함수
def creat_Map(list, address):
#남산타워 위도경도
    x = list[0]['x']#126.987867837993 
    y = list[0]['y']#37.5511225714939
    location=(y,x) # y가 위도 / x가 경도 (y, x)는 고정됨
    map=folium.Map(text, max_width=200) #zoom-start시작 시 줌 크기

    for store in list:
        location=(store['y'],store['x'])
        popup=folium.Popup(store['name'])
        text=f"{store['name']}<br>{store['phone']}<br>{store['address']}"
        folium.Marker(
            location,
            popup,
            icon=folium.Icon(color='blue', icon='glyphicon-road')
        ).add_to(map)
    map.save(f'data/map/{address}지역 매장현황.html') #html로 변환 저장해줌

if __name__=='__main__':
    list=getAddress()
    os.system('cls')
    while True:
        print()
        address=input('매장주소[賣場州所]>')
        if address=="":break
        search_list=searchAdress(address)
        if len(search_list)==0:
            print('검색된 매장이 없습니다!')#이거를 search_list함수에 넣으면 반복해서 나옴
        else:
            sel=input('지도를 출력하시겠습니까?(Y)>')
            if sel=='y' or sel=='Y':
                 creat_Map(search_list,address)