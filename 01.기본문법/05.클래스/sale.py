from product import Product #모듈 product에서 Product를 상속
from datetime import date #시스템 날짜를 가져오는 파이썬 프로그램
class Sale(Product): #생성자 선어
    def __init__(self, code, name, price, qnt):
        super().__init__(code, name, price)
        self.seq=0
        self.qnt=qnt
        self.date= date.today() #금일 날짜 가져오기
        self.sum = self.price * self.qnt

    def dict(self):
        child = super().dict() # parent는 code, name, product가 있음
        child ['seq'] = self.seq
        child['qnt'] = self.qnt
        child['date']= self.date
        child['sum']=self.sum
        return child

if __name__=='__main__':
    s = Sale('001','냉장고',250,10)
    print(s.dict())