#메일 전송하기
import smtplib
from account import *

#ex. naver.com / daum.net... // 포트는 587
with smtplib.SMTP('smtp.gmail.com',587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(EMAIL_ADDRESS,APP_PASSWORD)

#메일 제목,내용, 전송할 내용(subject,body,msg)
    subject='test email'
    body='main body'
    msg=f'Subject:{subject}\n{body}'
    smtp.sendmail(EMAIL_ADDRESS, 'naxen5611@naver.com', msg)

