from function import *
from product import *
from sale import Sale

products = [
    {'code':'001', 'name':'LG 냉장고','price':180},
    {'code':'002', 'name':'LG 세탁기','price':150},
] #딕셔너리의 리스트

sale =[]

def search(code): #코드를 통해 딕셔너리랑 비교해 찾아줌(p = dictionary)
    for p in products:
        if code == p['code']:
            return p

def max_seq():
    seqs = []
    for s in sale:
        seqs.append(s['seq'])
    if len(seqs)==0:
         return 0
    else:
        return max(seqs)

while True:
    menuPrint('매출관리')
    menu = input("메뉴선택>")
    if menu == "0": break #종료

    elif menu == "1": #매출등록
        code = input("상품코드>")
        if code =="": continue # 공란
        p = search(code)
        if p== None:
            print(f'{code}번 상품이 없습니다.') # 문자열 "" / '' 사용 // 
        else:
            name = p['name']
            price = p['price']
            print(f'상품명:{name} 가격:{price}')
            qnt = inputNum('수량>')
            if qnt=="": continue
            s = Sale(code, name, price, qnt)
            s.seq = max_seq()+1
            sale.append(s.dict())
            print('매출등록완료!')

    elif menu =='2': #검색
        name = input('검색이름>')
        isFind = False
        for s in sale:
            if s['name'].upper().find(name.upper()) != -1:
                print(f"{s['seq']},{s['code']},{s['name']},{s['price']:,}만원,", end="")
                print(f"{s['qnt']:,}개,{s['sum']:,}만원,{s['date']}")
                isFind = True
        if isFind == False: print('검색이름이 없습니다')

    elif menu =='3': #목록
        for s in sale:
            print(f"{s['seq']},{s['code']},{s['name']},{s['price']:,}만원,", end="")
            print(f"{s['qnt']:,}개,{s['sum']:,}만원,{s['date']}")
         
    elif menu == '4': #삭제
        seq = inputNum("삭제코드>")
        for idx, s in sale:
            if s['idx'] == seq:
             print(f"{s['seq']},{s['code']},{s['name']},{s['price']:,}만원,", end="")
             print(f"{s['qnt']:,}개,{s['sum']:,}만원,{s['date']}")
            sel = input('삭제하실래요?>')
            if sel == "Y" or sel == "y":
                        sale.pop[idx]
                        print('삭제완료!')

    elif menu == '5': #수정 #수정번호 받아서 continue
        seq = inputNum("수정번호>")
        if seq == "": continue
        for s in sale:
            print(f"상품코드':s{['code']}")
            print(f"상품명':s{['name']}")
            print(f"판매일':s{['date']}")
            qnt = inputNum(f"수정할 판매수량s{s['qnt']} >")
            if qnt != -1:
                s['qnt'] = qnt
                print('매출수정완료!')