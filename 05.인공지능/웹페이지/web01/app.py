from flask import Flask,render_template, request, send_file
import pandas as pd
from sklearn.linear_model import LinearRegression, SGDRegressor
import matplotlib.pyplot as plt
from io import BytesIO


plt.switch_backend('agg')
app=Flask(__name__, template_folder='temp')

plt.rc('font',family="Malgun Gothic")
plt.rc('axes', unicode_minus=False)

def model_linear():
    dataset=pd.read_csv(f'{app.root_path}/data/model.csv')
    X=dataset.iloc[:,:-1].values
    y=dataset.iloc[:,-1].values
    reg=LinearRegression()
    reg.fit(X,y)
    return reg

reg=model_linear()

@app.route('/linear/pred') #최소제곱법 model생성하여 예측하는 것을 의미
def pred_liner():
    hour=int(request.args['hour'])
    pred=reg[[hour]]
    print(pred[0])
    return f"{pred[0]:.2f}" #학습된 model을 소수 둘째자리까지 return

@app.route('/linear/graph')
def graph_liner():
    dataset=pd.read_csv(f'{app.root_path}/data/model.csv')
    X=dataset.iloc[:,:-1].values
    y=dataset.iloc[:,-1].values
    
    plt.scatter(X, y, label='실제점수')
    plt.plot(X, reg.predict(X), label='예측점수', color='g')
    plt.grid(True, ls='--', lw=0.5)
    plt.legend()
    plt.xlabel('공부시간')
    plt.ylabel('시험점수')

    img=BytesIO()
    plt.savefig(img, format='png')
    plt.close
    img.seek(0)
    return send_file(img, mimetype='image/png')

def model_sgd():
    dataset=pd.read_csv(f'{app.root_path}/data/model.csv')
    X=dataset.iloc[:,:-1].values
    y=dataset.iloc[:,-1].values

    sr=SGDRegressor()
    sr.fit(X,y)
    return sr

sr=model_sgd()

@app.route('/')
def index():
    PageName='home.html'
    return render_template('index.html', PageName=PageName)

@app.route('/linear')
def linear():
    pageName='linear.html'
    return render_template('index.html', PageName=pageName)

@app.route('/sgd/graph')
def graph_sgd():
    dataset=pd.read_csv(f'{app.root_path}/data/model.csv')
    X=dataset.iloc[:,:-1].values
    y=dataset.iloc[:,-1].values

    plt.scatter(X, y, label='실제점수')
    plt.plot(X, sr.predict(X), label='예측점수', color='g')
    plt.grid(True, ls='--', lw=0.5)
    plt.legend()
    plt.xlabel('공부시간')
    plt.ylabel('시험점수')

    img = BytesIO()
    plt.savefig(img, format='png')
    plt.close()
    img.seek(0)
    return send_file(img, mimetype='image/png')

@app.route('/sgd/pred')
def pred_sgd():
    hour=int(request.args['hour'])
    pred=sr.predict([hour])
    return f'{pred[0]:.2f}'

@app.route('/sgd')
def sgd():
    pageName='sgd.html'
    return render_template('index.html', PageName=pageName)

if __name__=='__main__':
    app.run(port=5000, debug=True)