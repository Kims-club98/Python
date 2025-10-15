# 외부 pymysql db table에 접근하는 방법
import pymysql

con=pymysql.connect(
    host='localhost',
    user='root',
    password='1234',
    db='haksa',
    charset='utf8',
    cursorclass=pymysql.cursors.DictCursor)
cur=con.cursor()
        # host = 서버위치 (타 게이트웨이 입력 시 접근하여 정보 이용 가능)
        # user = 사용자(본인: root)
        # passward: mysql의 비밀번호
        # db = 사용한 db명
        # charset = 언어 코드

#클래스 선언1(Dept) #학과코드 1 = 전자공학과 (Student 코드와 연계)
class Dept():
    def __init__(self):
        self.dcode=0
        self.dname=""

#클래스 선언2(Student)
class Student(Dept):
    def __init__(self):
        super().__init__()
        self.id=0
        self.name=""
        self.code=0
    def print(self):
        print(f"학번: {self.id} | 이름: {self.name} | 학과:{self.dname} ({self.code}) |")
        print('-'*50)



#리스트 가져오기
def list(key):
    try:
        keys=['id','name','dname']
        sql = f'select * from vstudent order by {keys[key+1]}'
        cur.execute(sql)
        rows=cur.fetchall()
        list=[]
        for row in rows:
            stu = Student()
            stu.id=row['id']
            stu.name=row['name']
            stu.dname=row['dname']
            stu.code=row['code']
            list.append(stu)
        return list
    except Exception as err:
        print("학생목록 오류발생", err)

# 학과 리스트 출력(code에서 dept)
def listDept():
    try:
        sql='select * from dept'
        cur.execute(sql)
        rows=cur.fetchall()
        list =[]
        for row in rows:
            dept = Dept()
            dept.dcode=row['dcode']
            dept.dname=row['dname']
            list.append(dept)
        return list
    except Exception as err:
        print('학과 리스트 출력 함수 오류 발생', err)

#찾기 함수(search 에서 검색하면 list를 출력, list 결과는 학생 객체를 출력)
def search(value):
    try:
        sql='select * from vstudent where id like %s or name like %s or dname like %s'
        value = f'%{value}%'
        cur.execute(sql,(value,value,value,))
        rows=cur.fetchall()
        if rows!=None:
            list=[]
        for row in rows:
            stu = Student()
            stu.id = row['id']
            stu.name = row['name']
            stu.code = row['code']
            stu.dname = row['dname']
            list.append(stu)
        return list

    except Exception as err:
        print('찾기함수 오류발생',err) 

# New ID 리턴 함수
def newID():
    try:
        sql='select convert(max(id)+1, char(4)) as new_id from student' # 그대로 진행 시 id값은 int 값으로 n.0 형태가 됨 So SQL에서 'covert'와 'char'를 통해 문자열로 변환시켜야 함
        cur.execute(sql)
        row=cur.fetchone()
        return row['new_id']

    except Exception as err:
        print('NewID함수 오류발생',err)

#학과코드 입력함수
def inputCode(title, menu):
        list=listDept()
        codes=[dept.dcode for dept in list] # dept dcode를 code에 넣는다
        print('-'*50)
        for dept in list:
            print(f"{dept.dcode}.{dept.dname}",end='|')
        print()
        print('-'*50)
        while True:
            code=input(title)
            if code=="": #조건 1
                print('학과코드를 입력하세요!')
                return code
            elif not code.isnumeric(): #조건 2
                print('학과코드를 숫자로 입력하세요!')
            elif codes.count(int(code))==0: #조건3
                print(f"{codes} 코드번호를 입력하세요!")
            else:
                return int(code) #조건을 제외한 나머지
                print('코드입력완료')
        

def insert(stu):
    try:
        sql = 'insert into student(id, name, code) values(%s, %s, %s)'
        cur.execute(sql,(stu.id,stu.name,stu.code,))
        con.commit() #삽입
        print('학생등록완료!')
        stu = Student()

    except Exception as err:
        print('삽입 함수 오류',err)
    
# 데이터를 읽는 함수 read
def read(id):
    try:
        sql='select * from vstudent where id=%s'
        cur.execute(sql,(id))
        row=cur.fetchone()
        if row !=None: #값이 있다
            stu=Student()
            stu.id=row['id']
            stu.name=row['name']
            stu.code=row['code']
            stu.dname=row['dname']
            return stu

    except Exception as err:
        print('읽기 함수 오류', err)

def delete(id):
    try:
        sql='delete from student where id=%s'
        cur.execute(sql,(id))
        con.commit()
        print('학생삭제완료!')

    except Exception as err:
        print('삭제함수 오류',err)

#수정하는 학생 검색 / 있는지 없는지 확인(있으면 있다 알리고 없으면 다시 입력) / 입력 X 시 기존이름 바로 사용-입력 시 변경/ 코드도 입력 X 그대로-입력 시 변경
def update(stu):
    try:
        sql='update student set name=%s, code=%s where id=%s'
        cur.execute(sql,(stu.name,stu.code,stu.id))
        con.commit()
        print('학생수정완료!')

    except Exception as err:
        print('수정함수 오류',err)

#-------------------------6번 dept 메뉴 함수------------------------------#

#학과등록 함수
def insertDept(dname):
    sql='insert into dept(dname) values(%s)'
    cur.execute(sql,(dname))
    con.commit()
    print('학과등록완료!')

#학과 읽기함수 *
def readDept(dcode):
    sql='select * from dept where dcode=%?'
    cur.execute(sql,(dcode))
    row=cur.fetchone()
    dept=Dept()
    dept.dcoe=row['dcode']
    dept.dname=row['dname']
    return dept

#학과 수정 함수 # stu 역할이 dept
def updateDept(dept):
    sql='update dept set dname=%s, where dcode=%s'
    cur.execute(sql,(dept.dname,dept.decode))
    con.commit()
    print('학과수정완료!')

def sale_insert(sale):
    try:
        sql='inert into sale(code, date, qnt, price) values(%s, date, %s, %s))'
        cur.execute(sql,(sale.code, sale.qnt,sale.price))
        con.commit()
        print('매출등록완료!')
    except Exception as err:
        print('세일 삽입 함수 오류',err)


#테스트용
if __name__=='__main__':
    stu = input('학과코드>')
    stu=read(id)
    if stu == None:
        print('학생이 없습니다!')
    else:
        stu.print()
        