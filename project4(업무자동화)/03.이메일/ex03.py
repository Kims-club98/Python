#메시지 만들고 send하여 보내기만 gka
from email.message import EmailMessage
from account import *
import smtplib

msg=EmailMessage()
msg['Subject']='파일첨부예제'
msg['From']=EMAIL_ADDRESS
msg['To']='naxen5611@gmail.com'
msg.set_content('테스트 내용입니다.')

#첨부파일 넣기
with open('manage.png','rb') as file:
    msg.add_attachment(file.read(),maintype='image',subtype='png',
                       filename=file.name)

with open('sample3.xlsx','rb') as file:
    msg.add_attachment(file.read(),maintype='application',subtype='octet-stream',
                       filename=file.name)


#ex. naver.com / daum.net... // 포트는 587
with smtplib.SMTP('smtp.gmail.com',587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(EMAIL_ADDRESS,APP_PASSWORD)
    smtp.send_message(msg)

