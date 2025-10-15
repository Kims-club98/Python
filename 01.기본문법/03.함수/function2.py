#숫자 입력/숫자가 입력될대까지 계속 입력 inputNum 
def inputNum(title): #함수정의(입력받는 대상)
    while True: #께속 함수를 실행하겠다 (While True)
        num = input(f'{title}>')
        if num.isnumeric(): # num이 숫자입력 시 
            return int(num) 
        elif num == "": # num에 공백입력 시
            return num
        else: #숫자, 공백 외 입력(문자입력) 시
            print("숫자로 입력하세요!")
# 설명: isnumeric을 통해 num이 숫자, 공백이면 return num(입력), 아니면 "숫자를 입력하세요" 메시지와 함께 반복

# Search 함수 [검색함수] (list 와 code를 입력받아 list에서 code를 검색하는 함수) <검색, 삭제, 수정 시 사용되더라...>
def search(list, code): 
    for index, item in enumerate(list): 
        if item['code']==code: 
            return index

# 메뉴 출력하는 함수 (def는 함수 선언) menuPrint
def menuPrint(title):
    print(f'**************{title}***************')
    print('|1.입력|2.검색|3.목록|4.삭제|5.수정|0.종료|')
    print('--------------------------------------')

# 새로운 코드의 함수 newCode #list에서 codes 추출, list codes에서 max 추출
def newCode(list):
    if len(list)==0:
        return 1
    
    codes = []

    for s in list:
        codes.append(s['code'])
    return max(codes)+1

# 아이템을 출력하는 함수 (item의 Key 구하기)
def itemPrint(item):
    keys = item.keys() #Keys는 목록, Key는 Keys에서 각각 대조
    for key in keys:
        if isinstance(item[key],int): #isinstance: item[key]값이 int type이면 True
            print(f"{item[key]:,}",end="\t")
        else:
            print(item[key], end="\t")
        print('\n----------------------------')
if __name__ == '__main__': #현 이 파일에서만 실행하겠음.(function2에서만 실행됨) test용 함수

    sale = [
    {'code':1, 'name':'냉장고', 'price':250, 'qnt':5},
    {'code':2, 'name':'세탁기', 'price':150, 'qnt':3},
]

    itemPrint(sale[0])
