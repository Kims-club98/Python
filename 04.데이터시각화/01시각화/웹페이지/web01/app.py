#서버 만들기
from flask import Flask, render_template, send_file
from io import BytesIO
import matplotlib.pyplot as plt
import matplotlib as mal
import pandas as pd

app= Flask(__name__, template_folder='templates') #템플릿에 담겨있는 폴더

#한글설정
plt.rc('font', family = 'Malgun Gothic')
plt.rc('font', size = 10)
plt.rc('axes', unicode_minus = False)


@app.route('/graph1') #학생별 막대 그래프
def graph1():
    df=pd.read_csv("C:/Python/04.데이터시각화/01시각화/data/score.csv",index_col='지원번호')
    name=df['이름']
    height=df['키']
    plt.figure(figsize=(10,3))
    plt.bar(name, height, color='purple',hatch='o')
    plt.xticks
    plt.ylim(150,210)
    for idx, h in enumerate(height):
        plt.text(idx, h+2, h, color='darkgray',ha='center')

    img=BytesIO()
    plt.savefig(img, format='png')
    plt.close()
    img.seek(0)
    return send_file(img, mimetype='image/png')

@app.route('/graph2')
def graph2():
    df=pd.read_csv("C:/Python/04.데이터시각화/01시각화/data/score.csv",index_col='지원번호')
    df['평균']=df.apply(lambda row:row['국어':'사회'].mean(),axis=1)
    name=df['이름']
    avg=df['평균']
    plt.figure(figsize=(10,3))
    plt.bar(name, avg, color='purple',hatch='o')
    plt.xticks
    plt.ylim(0,100)
    for idx, h in enumerate(avg):
        plt.text(idx, h+2, f'{h:.2f}점', color='darkgray',ha='center')

    img=BytesIO()
    plt.savefig(img, format='png')
    plt.close()
    img.seek(0)
    return send_file(img, mimetype='image/png')

@app.route('/graph3')
def graph3():
    df=pd.read_csv("C:/Python/04.데이터시각화/01시각화/data/score.csv",index_col='지원번호')
    df['평균']=df.apply(lambda row:row['국어':'사회'].mean(),axis=1)
    group=df.groupby('학교')['평균'].mean()
    sch=group.index
    avg=group.values
    plt.figure(figsize=(10,3))
    plt.bar(sch, avg, color='purple',hatch='o', width=0.3)
    plt.xticks(rotation=45, size=8, color='red')
    plt.ylim(0,100)
    for idx, h in enumerate(avg):
        plt.text(idx, h+2, f'{h:.2f}점', color='darkgray',ha='center')

    img=BytesIO()
    plt.savefig(img, format='png')
    plt.close()
    img.seek(0)
    return send_file(img, mimetype='image/png')

@app.route('/graph4')
def graph4():
    df=pd.read_csv("C:/Python/04.데이터시각화/01시각화/data/score.csv",index_col='지원번호')
    group=df.groupby('학교')['키'].mean()
    sch=group.index
    height=group.values
    plt.figure(figsize=(10,3))
    plt.bar(sch, height, color='purple',hatch='o', width=0.3)
    plt.xticks(rotation=45, size=8, color='red')
    plt.ylim(160,220)
    for idx, h in enumerate(height):
        plt.text(idx, h+2, f'{h:.2f}cm', color='darkgray',ha='center')

    img=BytesIO()
    plt.savefig(img, format='png')
    plt.close()
    img.seek(0)
    return send_file(img, mimetype='image/png')

@app.route('/graph5')
def graph5():
    df=pd.read_csv("C:/Python/04.데이터시각화/01시각화/data/score.csv",index_col='지원번호')
    df['SW특기']=df['SW특기'].str.capitalize()
    group=df.groupby('SW특기').size()
    sw=group.index
    peo=group.values
    plt.figure(figsize=(10,3))
    plt.bar(sw, peo, color='purple',hatch='o', width=0.3)
    plt.xticks(rotation=45, size=8, color='red')
    plt.ylim(0,10)
    for idx, h in enumerate(peo):
        plt.text(idx, h+2, f'{h}명', color='darkgray',ha='center')

    img=BytesIO()
    plt.savefig(img, format='png')
    plt.close()
    img.seek(0)
    return send_file(img, mimetype='image/png')

@app.route('/')
def index():
    return render_template('index.html',title='학생관리')#템플릿 렌더링

if __name__=='__main__':
    app.run(port=5000, debug=True) #deug=True는 디버그를 계속 반영 가능

