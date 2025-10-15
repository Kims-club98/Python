#score class(클래스에 대한 이름: 대문자)
from student import Student

class Score(Student): #학생 Score / 부모 Student

    #성적 개체를 생성하는 생성자
    def __init__(self):
        super().__init__() #super = Student(super().__init__()와 동일)
        self.kor = 0
        self.eng = 0
        self.mat = 0
         # no, name, dept, birthday는 정의 필요 X(Student에 이미 O)
    
    #성적 객체의 정보를 출력하는 함수 (매서드) (클래스 내부는 매서드)
    def info_print(self):
        super().info_print() #Studnet().info_print()
        print(f"국어:{self.kor}, 수학:{self.eng}, 영어:{self.mat}")

    #평균점수결과 P/F여부 매서드(함수)
    def result(self):
        avg = (self.kor+self.eng+self.mat)/3
        if avg < 70:
            return "Fail"
        else:
            return "Pass"

    # dictionary로 변환하는 매서드(함수)
    def dict(self):
        return {'no':self.no, 'name':self.name, 
                'kor':self.kor, 'eng':self.eng, 'mat':self.mat, 
                'avg':(self.kor+self.eng+self.mat)/3,
                'result':self.result()}


if __name__ == '__main__':
    s = Score() #부모의 변수를 적용받음(no, name, dept, birthday ok)
    s.no = '01' 
    s.name = '홍길동'
    s.kor = 90
    s.eng = 80
    s.mat = 20
    s.info_print()
    print(s.dict())