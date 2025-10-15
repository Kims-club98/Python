class Student:
    def __init__(self):
        self.no=""
        self.name=""
        self.dept="컴정과"
        self.birthday="00-01-04"
        
    def info_print(self): #학생 자체를 출력하는 매서드(=함수) [출력] end=','(1줄 표현 구분자 1줄)
        print(f"학번:{self.no}", end=',')
        print(f"성명:{self.name}", end=',')
        print(f"학과:{self.dept}", end=',')
        print(f"생년월일:{self.birthday}")
# 학생 class는 학생 객체, 이름을 생성 (Self, 매개 입력 시, 학번/성명/학과/생일이 출력됨)
    
    def info(self): #학생 정보를 생성하는 매서드(함수) 학생 정보를 dictionary로 생성해주는 함수 [정보 dictionary로]
        return {'no':self.no, 'name':self.name, 'dept':self.dept, 'birthday':self.birthday}

#클래스: 객체를 생성하는 틀 (형식이 일정하므로 관리가 편리함)
#메소드: 클래스 내부에 있는 함수
#self: 생성된 객체 자신



if __name__ == '__name__':
    s =Student()
    s.no='o1' 
    s.name='홍길동'
    s.birthday='02-12-17'
    s.info_print()


