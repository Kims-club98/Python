# Search 함수 [검색함수] (list 와 code를 입력받아 list에서 code를 검색하는 함수) <검색, 삭제, 수정 시 사용되더라...>
def search(list, code): 
    for index, item in enumerate(list): 
        if item['code']==code: 
            return index
        
sale = [
    {'code':1, 'name':'냉장고', 'price':250, 'qnt':5},
    {'code':2, 'name':'세탁기', 'price':150, 'qnt':3},
]

index= search(sale, 20) # sale의 code에서 찾는다
if index == None:
    print('해당 데이터가 없습니다')
else:
    print(sale[index])
    