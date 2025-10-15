from score import Score #Score class 사용 가능
from function import *

# 학번, 이름, 국, 영, 수를 받아 dict에 입력됨
def insert(list):
    score = Score()
    score.no = input('학번>')
    score.name = input('이름>')
    score.kor = int(input('국어>'))
    score.eng = int(input('영어>'))
    score.mat = int(input('수학>'))
    print(score.dict())
    list.append(score.dict())

scores= []
while True:
    menuPrint('성적관리')
    menu = input("메뉴선택>")
    if menu == "0": 
        break

    elif menu == "1":
        insert(scores)

    elif menu == "3":
        for s in scores:
            print(s)

    elif menu == '2':
        no = input('검색학번>')
        for s in scores:
            if no == s['no']:
                print(s) 

    elif menu == '4':
        no =input('삭제번호>')
        for idx, s in enumerate(scores):
            if no == s['no']:
                scores.pop(idx)

