from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__, template_folder='temp', static_folder='static')

#데이터 테이블 출력
@app.route('/data')
def data():
    page = int(request.args['page'])
    size = int(request.args['size'])
    start =(page-1) * size #0, 5, 10
    end =(page*size) #4, 9, 14
    df = pd.read_csv('data/타이타닉/test.csv')
    total = len(df)
    df = df[start:end]
    table = df.to_html(classes='table table-striped table-hover', index=True)
    data = {'table':table, 'total':total}
    return data

# 예측(최종: 예측성공 메시지 출력)
@app.route('/predict')
def predict():
    #학습모델로 학습시키기
    from sklearn.neighbors import KNeighborsClassifier
    model=KNeighborsClassifier()
    
    test=pd.read_csv('data/타이타닉/테스트.csv')
    train=pd.read_csv('data/타이타닉/훈련.csv')
    X=train.iloc[:,1:].values
    y=train.iloc[:,0].values
    #학습모델만들기
    model.fit(X,y)

    X_pred=test.iloc[:,:].values
    y_pred=model.predict(X_pred)

    df_test=pd.read_csv('data/타이타닉/test.csv')
    df_test.to_csv('data/타이타닉/test.csv', index=False)
    return 'success'

@app.route('/reset')
def reset():
     df_test=pd.read_csv('data/타이타닉/test.csv')
     df_test['pred']=''
     df_test.to_csv('data/타이타닉/test.csv', index=False)
     return df_test


@app.route('/')
def index():
    return render_template('index.html', pageName='home.html', title='타이타닉 생존예측')

if __name__=='__main__':
    app.run(port=5000, debug=True)