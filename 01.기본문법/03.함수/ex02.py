#자료를 통해 총점과 학점을 입력 (dic)
students=[
 {"no":"1번", "이름":"홍길동", "국어":90, "영어":95, "수학": 98},
 {"no":"2번", "이름":"강감찬", "국어":80, "영어":99, "수학": 96},
 {"no":"3번", "이름":"이순신", "국어":92, "영어":85, "수학": 78},
 {"no":"4번", "이름":"성춘향", "국어":78, "영어":55, "수학": 67},
 {"no":"5번", "이름":"이몽룡", "국어":95, "영어":85, "수학": 87},
 ]

#학점을 구하는 함수
def grade(score): #새로운 함수 정의함(기존 파이썬의 함수를 사용하면 안됨)(함수정의한다: def) _ 정의만 한 상황, 호출을 해야함
    grade = "" #그냥 grade라는 변수명을 만들어줌
    if score >=90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"
    return grade #값을 되돌려줌 중요중요

#반복작업 for문
for s in students: # students 에서 추출함
    tot = s['국어'] + s['영어'] + s.get('수학')
    avg = tot/3
    level = grade(avg)
    print(s['no'],s['이름'], tot, f'{avg:.2f}',level)
