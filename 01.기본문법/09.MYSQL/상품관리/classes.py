class Product:
    def __init__(self):
        self.code=0
        self.name=""
        self.price=0
    
    def print(self):
        print(f"코드: {self.code}, 상품명: {self.name}, 가격: {self.price:,}원")

class Sale(Product):
    def __init__(self):
        super().__init__()
        self.seq=0
        self.date=""
        self.qnt=0
        self.sum=self.price*self.qnt
        
    def print(self):
        print(f"NO:{self.seq}, 코드: {self.code}, 상품명: {self.name},판매일: {self.date}")
        print(f'판매가:{self.price:,}, 판매수량: {self.qnt}개, 금액: {self.sum:,}원')
        print('-'*50)
    
