from flask import Blueprint,render_template, send_file,request
from io import BytesIO
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import numpy as np

bp=Blueprint('kmeans',__name__,url_prefix='/kmeans')

#K평균 모델만들기
@bp.route('/kmeans')
def model_kmeans(K):
    kmeans=KMeans(n_clusters=K, random_state=0) # 클러스터 개수(n_clusters)를 K개로 설정, random_state로 재현 가능

    dataset=pd.read_csv('data/KMeansData.csv')
    X=dataset.iloc[:,[0,1]].values

    from sklearn.preprocessing import StandardScaler # 데이터 정규화를 위한 StandardScaler를 가져옴
    scaler=StandardScaler() # StandardScaler 객체 생성(평균:0, 표준편차: 1로 설정)
    X_trans=scaler.fit_transform(X) #원본 데이터 X에 대해 표준화 수행 후(평균, 표준편차) X_trans로 정의

    kmeans.fit(X_trans) #표준화된 모델 X_trans를 K-means 모델로 학습

    X_org=scaler.inverse_transform(X_trans) #표준화된 X_trans를 원본으로 되돌림(X_org = X)
    center_org=scaler.inverse_transform(kmeans.cluster_centers_) #K-mean로 찾은 클러스터 중심점, 원래 스케일로 되돌림(center_org 정의)
    return kmeans, X_org, X_trans, center_org #학습된 모델(kmeans) 

@bp.route('/cluster')
def cluster():
    from sklearn.cluster import KMeans #데이터의 거리의 제곱의 합을 구하는 라이브러리(k-means X 아님)
    import pandas as pd
    inertia_list=[] # 각 점들에서 중심점까지의 거리들의 합 리스트(중심점 - 각 점 거리 합) # inertia=각 중심점거리의 합
    dataset=pd.read_csv('data/KMeansData.csv')
    X=dataset.iloc[:,[0,1]].values

    from sklearn.preprocessing import StandardScaler # 데이터 정규화를 위한 StandardScaler를 가져옴
    scaler=StandardScaler() # StandardScaler 객체 생성(평균:0, 표준편차: 1로 설정)

    X_trans=scaler.fit_transform(X) #원본 데이터 X에 대해 표준화 수행 후(평균, 표준편차)

    for i in range(1,11,1):
        kmeans=KMeans(n_clusters=i,init='k-means++',random_state=0)
        kmeans.fit(X_trans)
        inertia_list.append(kmeans.inertia_)

    x=range(1,11,1) #배열로 1-10까지 들어감
    y=inertia_list
    plt.switch_backend('agg')
    plt.figure(figsize=(5,3))
    plt.plot(x,y,marker='o') # X와 Y의 리스트가 같아야 함
    plt.xticks([x for x in range(1,11,1)])
    plt.grid(True,ls='--',lw=0.5)
    plt.xlabel('n_cluster')
    plt.ylabel('inertia')
    # plt.show()
    img=BytesIO()
    plt.savefig(img,format='png',bbox_inches="tight")
    plt.close()
    img.seek(0)
    return send_file(img, mimetype='image/png')

@bp.route('/graph')
def graph():
    no=int(request.args['no'])
    kmeans, X_org,X_trans,centers_org=model_kmeans(no)
    y_pred=kmeans.fit_predict(X_trans)
    
    plt.figure(figsize=(10, 7))
    for i in range(no):
        index = np.where(y_pred==i)
        x=X_org[index, 0]
        y=X_org[index, 1]
        plt.scatter(x, y, s=200, ec="black")
        plt.title('Score by study time', size=20)
        cx = centers_org[i, 0]
        cy = centers_org[i, 1]
        plt.scatter(cx, cy, c='yellow', s=600, ec='black', marker='s')
        plt.text(cx, cy, i, ha='center', va='center')
        plt.xlabel('HOUR')
        plt.ylabel("SCORE")
    for idx, x in enumerate(X_org):
        plt.text(x[0],x[1],idx, ha='center',va='center',color='white', size=5)
    img=BytesIO()
    plt.savefig(img,format='png')
    plt.close()
    img.seek(0)
    return send_file(img, mimetype='image/png')

@bp.route('/data')
def data():
    no=int(request.args['no'])
    kmeans,X_trans=model_kmeans(no)
    y_pred=kmeans.predict(X_trans)

    df=pd.read_csv('data/K-평균.csv')
    df['그룹']=y_pred
    df=df[:10]
    table=df.to_html(classes="table table-striped table-hover",index=False)
    data={'table':table}
    return data


@bp.route('/')
def kmeans():
    df=pd.read_csv('data/K-평균.csv')
    df=df[:10]
    table=df.to_html(classes="table table-striped table-hover",index=False)
    return render_template('index.html',pageName='kmeans.html',title='K-평균'
                            ,table=table)
