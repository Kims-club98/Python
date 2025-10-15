from flask import Flask, render_template, request,send_file
import pandas as pd
import FinanceDataReader as fdr
from io import BytesIO
import matplotlib.pyplot as plt
from NAVERapi import getNew
from model import creat_model
import re



app = Flask(__name__, template_folder='temp', static_folder='static')

vector,model=creat_model()

@app.rout('/predict')
def predict():
    text=request.args['text']
    #한글만 출력
    find_text=re.findall(r"[가-힣]+",text)
    join_text=[' '.join(find_text)]
    vector_text=vector.transform(join_text)
    pred=model.predict(vector_text)
    if pred[0]==0:
        return '부정'
    else:
        return '긍정'
    


@app.route('/search')
def search():
    page=int(request.args['page'])
    start=(page-1)*5+1
    query=request.args['query']
    page=request.args['page']
    items, totals=getNew(query,start,display)
    data={'items':items,'totals':totals}
    return data


@app.route('/')
def index():
    return render_template('index.html', pageName='home.html', title='감성분석')

if __name__=='__main__':
    app.run(port=5000, debug=True)