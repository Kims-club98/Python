from flask import Flask, render_template, request,send_file
import pandas as pd
import FinanceDataReader as fdr
from io import BytesIO
import matplotlib.pyplot as plt
plt.switch_backend('Agg')


app = Flask(__name__, template_folder='temp', static_folder='static')

def getData(code, start, end):
    code=request.args['code']
    start=request.args['start']
    end=request.args['end']
    df=fdr.DataReader(code,start,end) #회사 데이터 가져오기
    return df

@app.route('/data')
def data(): #front에서 input가져오기
    code=request.args['code']
    start=request.args['start']
    end=request.args['end']
    df=getData(code,start,end)
    df=df.head()
    table=df.to_html(classes="table table-striped table-hover")
    return table

@app.route('/img1')
def img1():
    code=request.args['code']
    start=request.args['start']
    end=request.args['end']
    df=getData(code,start,end)
    df['year']=df.index.year
    df['month']=df.index.month
    #Close에 대한 평균
    group=df.groupby(['year','month'])[['Close','Volume']].mean()
    group.reset_index(inplace=True)
    group
    plt.figure(figsize=(10,4))
    plt.plot(group.index,group["Close"],marker='o')
    xticks=[x for x in group.index] #range()
    plt.xticks(xticks,[f'{group.loc[idx, "year"]}-{group.loc[idx,"month"]}' for idx in xticks],rotation=45)

    img=BytesIO()
    plt.savefig(img, format='png')
    plt.close
    img.seek(0)
    return send_file(img, mimetype='image/png')

@app.route('/img2')
def img2():
    code=request.args['code']
    start=request.args['start']
    end=request.args['end']
    df=getData(code,start,end)
    df['year']=df.index.year
    df['month']=df.index.month
    #Close에 대한 평균
    group=df.groupby(['year','month'])[['Close','Volume']].mean()
    group.reset_index(inplace=True)
    plt.figure(figsize=(10,4))
    plt.bar(group.index,group["Volume"], width=0.5)
    xticks=[x for x in group.index] #range()
    plt.xticks(xticks,[f'{group.loc[idx, "year"]}-{group.loc[idx,"month"]}' for idx in xticks],rotation=45)
    img=BytesIO()
    plt.savefig(img, format='png')
    plt.close
    img.seek(0)
    return send_file(img, mimetype='image/png')

@app.route('/')
def index():
    return render_template('index.html', pageName='home.html', title='주가예측')

if __name__=='__main__':
    app.run(port=5000, debug=True)