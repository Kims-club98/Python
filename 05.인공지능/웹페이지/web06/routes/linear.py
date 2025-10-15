#선형회귀함수(서브라우터)
from flask import Blueprint, render_template,request #서브 라우터 정의를 위한 라이브러리, #템플릿은 전달하는 라이브러리 같이 넣어줘야 함
import pandas as pd
from sklearn.linear_model import LinearRegression, SGDRegressor #선형회귀 머신러닝을 위한 패키지

bp=Blueprint('linear',__name__,url_prefix='/linear') #(이름,__name__,url_print='연결될 주소')
#________________________________________________________________________________머신러닝

def model_reg():
    dataset=pd.read_csv("C:/Python/05.인공지능/웹페이지/web02/data/LinearRegressionData.csv",on_bad_lines='skip')
    X=dataset.iloc[:,:-1].values
    y=dataset.iloc[:,-1].values
    reg=LinearRegression()
    reg.fit(X,y)
    return reg

def model_sgd():
    dataset=pd.read_csv("C:/Python/05.인공지능/웹페이지/web02/data/LinearRegressionData.csv",on_bad_lines='skip')
    X=dataset.iloc[:,:-1].values
    y=dataset.iloc[:,-1].values
    sgd=SGDRegressor()
    sgd.fit(X,y)
    return sgd

@bp.route('/sgd/predict')
def sgd_predict():
    sgd=model_sgd()
    hour=float(request.args['hour'])
    pred=sgd.predict([[hour]])
    return f'{pred[0]:.2f}'

#___________________________경사 하강법
# hour로 부터 예측값을 받아서(input so int 변환 必) 예측(predict) 받는 함수
@bp.route('/reg/predict')
def reg_predict():
    reg=model_reg()
    hour=float(request.args['hour'])
    pred=reg.predict([[hour]])
    return f'{pred[0]:.2f}'

#________________________________________________________________________________라우터
#1. 최소제곱법 페이지출력 라우터(temp-reg로 이어짐) (linear 에서 reg.html로 이어짐)
@bp.route('/reg')     #인덱스 출력, reg.html을 출력
def reg():
    return render_template('index.html', pageName='reg.html',title='최소제곱법(선형회귀)')

#2. 경사하강법 페이지출력 라우터(temp-reg로 이어짐) (linear 에서 reg.html로 이어짐)
@bp.route('/sgd')
def sgd():
    return render_template('index.html',pageName='sgd.html',title='경사하강법(선형회귀)')