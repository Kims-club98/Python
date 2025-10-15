from flask import Blueprint,render_template,request
bp=Blueprint('logistic',__name__,url_prefix="/logistic") #blueprint 기본 setting

def model_logistic():
    import pandas as pd
    dataset=pd.read_csv('data/LogisticRegressionData.csv')
    X=dataset.iloc[:,:-1].values
    y=dataset.iloc[:,-1].values

    #모델생성하기
    from sklearn.linear_model import LogisticRegression
    logistic=LogisticRegression()
    logistic.fit(X,y)
    return logistic
#(Html input 이곳에서 받아서 시간에 대한 합격 가능성을 예측 후 보내줌)

@bp.route('/predict')
def predict():
    hour=float(request.args['hour']) #hour의 위치는 request에 있음(정수[int]가 아닌 실수 float으로 받기)(int로는 정수만 받음)
    model=model_logistic()
    pred=model.predict([[hour]]) #예측은 hour을 받아 predict를 진행함
    pred_proba=model.predict_proba([[hour]])
    data={'result': int(pred[0]),
          'fail':f'{pred_proba[0][0]*100:.2f}%',
          'pass':f'{pred_proba[0][1]*100:.2f}%'}
    print(data)
    return data
#predict는 0 or 1 0은 불합, 1은 합 // 불합격 확률 // 합격확률

@bp.route('/predict/data')
def predict_data():
    import pandas as pd
    df=pd.read_csv('data/로지스틱회귀.csv')
    logistic=model_logistic()
    X=df.loc[:,'공부시간'].values
    X2=X.reshape(len(X),1)
    y_pred=logistic.predict(X2)
    y_pred_proba=logistic.predict_proba(X2)
    y_pred_pass=[f'{y[1]*100:.2f}%' for y in y_pred_proba]
    df['pass']=y_pred
    df['합격예상']=df['pass'].apply(lambda x:'합격' if x==1 else '불합격')
    df['예상합격률']=y_pred_pass
    df.drop(columns='pass',inplace=True)
    return df.to_html(classes="table table-striped table-hover",index=False)

@bp.route('/')
def logistic():
    import pandas as pd
    df=pd.read_csv('data/로지스틱회귀.csv')
    table=df.to_html(classes="table table-striped table-hover",index=False)

    return render_template('index.html',pageName='logistic.html',
                           title='로지스틱 회귀', table=table) #로지스틱회귀 테이블을 불러와 return함
