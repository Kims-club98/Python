from flask import Blueprint, render_template, request
bp=Blueprint('multi',__name__,url_prefix='/multi')

#____________________________________________________________________다중회귀모형 모델 생성하기
def model_liner():
    import pandas as pd
    from sklearn.linear_model import LinearRegression
    from sklearn.compose import ColumnTransformer
    from sklearn.preprocessing import OneHotEncoder

    dataset=pd.read_csv("C:/Python/05.인공지능/웹페이지/web02/data/MultipleLinearRegressionData.csv",on_bad_lines='skip')
    X=dataset.iloc[:,:-1].values
    y=dataset.iloc[:,-1].values

    ct=ColumnTransformer(
        transformers=[('encoder', OneHotEncoder(drop='first'),[2])],
        remainder='passthrough')
    
    X_trans=ct.fit_transform(X)

    reg=LinearRegression()
    reg.fit(X_trans,y)
    return reg

@bp.route('/predict')
def predict():
    hour=int(request.args['hour']) # 공부시간
    place=request.args['place'] # 장소
    absent=int(request.args['absent']) #결석 적용
    places={'집':[0,1],'도서관':[1,0],'카페':[0,0]}
    p1=places.get(place)[0]
    p2=places.get(place)[1]
    model=model_liner()
    pred=model.predict([[p1,p2,hour,absent]])
    return f'{pred[0]:.2f}'


#다중선형회귀
@bp.route('/')
def multi():
    return render_template('index.html',pageName='multi.html',title='다중선형회귀')