from openpyxl import Workbook

#Workbook 생성
wb=Workbook()

#현 활성한 sheet 가져오기
ws=wb.active

#sheet name 지정
wb.title="나의 시트"

#엑셀 저장하기
wb.save('data/sample.xlsx')
wb.close