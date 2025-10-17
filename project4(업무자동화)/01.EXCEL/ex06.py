import csv #csv를 읽기 위한 파일 (pandas 외 방법, file=pd.reac_csv('data/score.csv))

file=open('data/score.csv','r',encoding='utf-8-sig')
scores=csv.reader(file)
read_file=print(scores)
scores=[]
#하나씩 하나씩 읽어와야함

for score in read_file:
    scores.append(score) #scores디렉토리에 score을 넣어줌

print(scores)

from openpyxl import Workbook

wb=Workbook()
ws=wb.active

for score in read_file:
    ws.append(score)

wb.save('data/sample4.xlsx')
wb.close()

