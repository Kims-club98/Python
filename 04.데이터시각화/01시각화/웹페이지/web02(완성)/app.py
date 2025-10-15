from flask import Flask, render_template, send_file
from io import BytesIO #이미지를 생성해주는 도구(기본 라이브러리)
import matplotlib.pyplot as plt
import matplotlib as mal
import pandas as pd

app=Flask(__name__, template_folder='Temp') #템플릿 파일 구성 / Temp파일을 만들고(명명도 동일) 하단에 index.html과 연결

@app.route('/')
def index():
    return render_template('index.html',title='그래프 연습') #주소가 route /일때, render_template가 index.html과 연결되어 그곳에 쓰여있는 내용이 서버에 출려이 됨

@app.route('/graph1') #주소창에 /graph1을 입력 시 아래 함수가 출력됨(위 /도 마찬가지임) #graph1이 되면 아래의 누적막대 그래프가 출력됨
def graph1():
    df=pd.read_csv("C:/Python/04.데이터시각화/01시각화/data/score.csv")
    plt.rc('font',family='Malgun Gothic') # 폰트 선택ㅇ
    plt.rc('font',size=11) #폰트크기 11
    plt.rc('axes',unicode_minus=False) #한글 깨짐 방지
    plt.figure(figsize=(10,5))
    plt.bar(df['이름'],df['국어'],label='국어')
    plt.bar(df['이름'],df['영어'],label='영어',bottom=df['국어'])
    plt.bar(df['이름'],df['수학'],label='수학',bottom=df['국어']+df['영어'],)
    plt.legend()
    plt.ylim(0,300)
    # plt.show()

    img= BytesIO() #그래프를 웹으로 이동
    plt.savefig(img, format='png') # 그래프를 
    plt.close()
    img.seek(0)
    return send_file(img, mimetype='image/png')



@app.route('/graph2') #주소창에 /graph1을 입력 시 아래 함수가 출력됨(위 /도 마찬가지임) #graph1이 되면 아래의 누적막대 그래프가 출력됨
def graph2():
    df=pd.read_csv("C:/Python/04.데이터시각화/01시각화/data/score.csv")
    x=df.index*4
    plt.bar(x+0,df['국어'],width=1,label='국어') # x축이 0,4,8,16,32...칸마다 기입됨
    plt.bar(x+1,df['영어'],width=1,label='영어')
    plt.bar(x+2,df['수학'],width=1,label='수학')
    xticks =[xticks+1 for xticks in x]
    plt.xticks(xticks, df['이름']) #x축의 x값과 이름 지정
    plt.legend()
    # plt.show()


    img= BytesIO() #그래프를 웹으로 이동
    plt.savefig(img, format='png') # 그래프를 
    plt.close()
    img.seek(0)
    return send_file(img, mimetype='image/png')


@app.route('/graph3') #주소창에 /graph1을 입력 시 아래 함수가 출력됨(위 /도 마찬가지임) #graph1이 되면 아래의 누적막대 그래프가 출력됨
def graph3():
    df=pd.read_csv("C:/Python/04.데이터시각화/01시각화/data/score.csv")
    group=df.groupby('SW특기').size()

    plt.pie(group.values,labels=group.index, autopct="%.1f%%",
            explode=[0.05]*len(group), wedgeprops={'width':0.8},
            )

    img= BytesIO() #그래프를 웹으로 이동
    plt.savefig(img, format='png') # 그래프를 
    plt.close()
    img.seek(0)
    return send_file(img, mimetype='image/png')

@app.route('/graph4') #주소창에 /graph1을 입력 시 아래 함수가 출력됨(위 /도 마찬가지임) #graph1이 되면 아래의 누적막대 그래프가 출력됨
def graph4():
    df=pd.read_csv("C:/Python/04.데이터시각화/01시각화/data/score.csv")
    df['학년'] = [3,3,2,1,1,3,2,2]

    plt.scatter(df['국어'],df['영어'], sizes=df['학년']*500, c=df['학년'], alpha=0.3, cmap='spring')
    plt.colorbar(ticks=[1,2,3],orientation='horizontal',label='철산고 학년',shrink=1)
    for idx in range(len(df)):
        x=df.loc[idx,'국어']
        y=df.loc[idx,'영어']
        name=df.loc[idx,'이름']
        plt.text(x,y,name, ha='center', size=8)
    plt.ylim(0,120)

    img= BytesIO() #그래프를 웹으로 이동
    plt.savefig(img, format='png') # 그래프를 
    plt.close()
    img.seek(0)
    return send_file(img, mimetype='image/png')


if __name__=='__main__':
    app.run(port=5000, debug=True) #앱 작동 포트 5000번, 디버그는 실시간으로 실행

 