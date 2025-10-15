#클래스
class Product:
    def __init__(self, code, name, price): #init 중요
        self.code = code
        self.name = name
        self.price = price

# 매서드(함수) - 객체 1개(self) 하나로 처리 가능
    def dict(self):
        return {'code':self.code, 'name': self.name, 'price': self.price}
    
if __name__=='__main__': #이곳에서만 실행 시 사용(클래스, 매서드가 잘 작동하는가? 체크)
    p = Product('p01','냉장고',250) #클래스 변수 
    print(p.dict())
