score = int(input('점수>'))
grade =''
if score >= 95:
    grade ='A+'
else:
    grade ='A0'
elif score >= 80:
    if score >=85:
    grade = 'B+'
    else:
        grade = 'b0'
elif score >= 70:
