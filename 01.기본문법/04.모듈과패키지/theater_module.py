#입장료를 계산하는 모듈
    #일반가격
def price(people):
    print(f"{people}명 가격은 {people * 15000:,}원 입니다.") #:, 천 단위로 쉼표 찍어줌

    #조조할인
def price_morning(people):
    print(f"{people}명 조조할인가격은 {people * 10000:,}입니다.")

    #군인할인
def price_soilder(people):
     print(f"{people}명 군인할인가격은 {people * 4000:,}입니다.")


if __name__ == '__main__':
    price_soilder(3)