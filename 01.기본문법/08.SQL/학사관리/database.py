import sqlite3
import os

path=os.path.dirname(os.path.realpath(__file__))
db_name= path + '/haksa.db'
con=sqlite3.connect(db_name)

con=sqlite3.connect(db_name) #원칙 con, 커서를 열고 마지막에 닫아야 함
cur=con.cursor() #커서 오픈을 미리 함


class Dept:
    def __init__(self):
        self.code=0
        self.dname=""

class Students(Dept):
    def __init__(self):
        super().__init__()
        self.id=""
        self.name=""
        self.dept=0
    
    def print(self): #형식에 맞게 출력
        print(f"학번:{self.id}, 학과명:{self.dname},({self.dept}), 이름:{self.name}")

# ㅇ
def listDept():
    try:
        sql='select * from dept' #학과 table 모든 것을 가져옴
        cur.execute(sql)
        rows=cur.fetchall()
        list=[]
        for row in rows:
            dept=Dept()
            dept.code=row[0]
            dept.dname=row[1]
            list.append(dept)
        return list
    except Exception as err:
        print('학과목록 에러',err)


def list(): # 리스트로 가져오기
    try: # 오류처리(try-except): 목적-에러 발생하여도 프로그램 정지 X
        sql='select * from vstudent'
        cur.execute(sql)
        rows= cur.fetchall() #여러 행이 출력되면 rows로 정의
        list =[]
        for row in rows:
            stu = Students() #Student (클래스) 기반으로 stu를 만듦
            stu.id=row[0]
            stu.dept=row[1]
            stu.name=row[2]
            stu.dname=row[3]
            list.append(stu)
        return list # list 모두 빼줌
    except Exception as err: #에러 발생시
        print('목록에러', err)
    finally:
        pass

#새로운 id 생성(자동생성목적)
def newID():
    try:
        sql ='select max(id)+1 from student'
        cur.execute(sql)
        row = cur.fetchone()
        new_id = row[0]
        return new_id
    except Exception as err:
        print('코드생성:', err)
    finally:
        pass


# 등록 함수(학생정보 필요) stu는 학생정보 O
def insert(stu):
    try: #오류검증함수
        sql='insert into student(id, name, dept) values(?,?,?);'
        cur.execute(sql,(stu.id,stu.name,stu.dept,))
        con.commit()
    except Exception as err:
        print('입력오류', err)
    finally:
        pass



#찾기 함수
def search(value):
    try:
        sql ='select * vstudent where name like ? or id like ? or dname like ? ' #모든 데이터 가지고 옴
        value=f'%{value}%'
        cur.execute(sql,(value, value, value,))
        rows=cur.fetchall()
        list=[]
        for row in rows:
            stu = Students() #Student (클래스) 기반으로 stu를 만듦
            stu.id=row[0]
            stu.dept=row[1]
            stu.name=row[2]
            stu.dname=row[3]
            list.append(stu)
        return list
    except Exception as err:
        print('검색오류',err)
    finally:
        pass

#학번 읽기 목적
def read(id):
    try:
        sql = 'select id, name, dept, dname from vstudent where id=?' 
        cur.execute(sql,(id,))
        row=cur.fetchone()
        if row!=None:
            stu = Students()
            stu.id =id
            stu.name=row[1]
            stu.dept=row[2]
            stu.dname=row[3]
            return stu
    except Exception as err:
        print('학번오류', err)

# 삭제 delete
def delete(id):
    try:
        sql = 'delete from student where id=?'
        cur.execute(sql,(id,))
        con.commit()
    except Exception as err:
        print('학번 읽기 오류',err)


#업데이트 Update
def update(stu): # 학생정보 전부
    try:
        sql='update student set name=?, dept=?, where id=?' # id를 통해 name과 dept를 바꾸겠다
        cur.execute(sql,(stu.name, stu.dept, stu.id,))
        con.commit()
    except Exception as err:
        print('학생수정오류', err)


# 학과코드입력
def inputDept(title, type):
    depts=listDept()
    for dept in depts:
        print(f"{dept.code}.{dept.dname}",end="|")
    print()
    codes=[dept.code for dept in depts] #if문 대체 

    while True:
        code=input(title)
        if code=="" and type==5:
            return ""
        elif code=="" and type==1:
            print('학과코드를 반드시 입력하세요')     
        elif not code.isnumeric():
            print('학과코드를 반드시 숫자로 입력하세요')
            
        elif codes.count(int(code))==0: #문자열 찾기 .find / 숫자찾기 .count
            print(f"{min(codes)}~{max(codes)}번을 입력하세요")
        else:
            return int(code)

    
if __name__=='__main__':
    newID(Students(id))