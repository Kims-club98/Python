from openpyxl import Workbook
from random import * #랜덤값을 출력해주는 기본패키지

#엑셀 파일 생성 및 활성화
wb=Workbook()
ws=wb.active

ws.append(['번호','영어점수','수학점수']) #열제목 생성
for i in range(1,11): #i(번호) 1-10번까지
    ws.append([i,randint(0,100),randint(0,100)]) #append는 한 행씩 값을 넣어줌, 랜덤값 0,100점사이중 넣어줌)

wb.save('data/sample3.xlsx')
wb.close()