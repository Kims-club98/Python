def model_liner(): # 변수 선언
    import pandas as pd #데이터 분석
    from sklearn.linear_model import LinearRegression # 학습데이터 모델링 분석

    dataset=pd.read_csv("data/LinearRegressionData.csv")
    X=dataset.iloc[:,:-1].values 
    y=dataset.iloc[:,-1].values # X,y 값 가져올 때 values값만 가지고 옴

    reg=LinearRegression() #모델 틀을 생성
    reg.fit(X, y) #독립변수/ 종속변수로 학습을 시작
    return reg

def predict(hour):
    model=model_liner()
    pred=model.predict([[hour]])
    print(f'{hour}시간 공부했을때 예상 점수 : {pred[0]:.2f}')


while True:

    hour=input('공부시간>')
    if hour=="":
        break
    elif not hour.isnumeric(): # hour가 숫자가 아니라면
        print('숫자로 입력하세요!')
    else:
        predict(int(hour))
        
