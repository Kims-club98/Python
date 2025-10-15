from flask import Flask, render_template,request
from tmdbv3api import Movie,TMDb
import pandas as pd
import pickle


app=Flask(__name__, template_folder='temp')

#줄거리 추천 함수(줄거리 추천 버튼을 누를 때 출력해주기)
@app.route('/overview/data')
def sim_recommend():

    title=request.args['title'] #front에 있는 title input 내역을 받아옴(받아오는 함수 request)
    df = pd.read_csv('data/movie/tmdb_5000_movies.csv')
    idx=df[df['title']==title].index[0]

    cosine_sim = pickle.load(open('data/movie/cosine_sim.pickle', 'rb'))
    sim = cosine_sim[idx]

    sim = list(enumerate(sim))
    sim = sorted(sim, key=lambda x: x[1], reverse=True)
    sim = sim[1:13]#1-12개를 받아옴
    index = [x[0] for x in sim]

    tmdb=TMDb()
    tmdb.api_key='c668cda4cf75bf267ef2aeffa2da0341'
    tmdb.language='ko-KR'
    movie=Movie()

    details=[]
    df=df.loc[index,'id']
    for id in df:
        detail=movie.details(id)
        ko_title=detail['title']
        poster='https://image.tmdb.org/t/p/w500' + detail['poster_path']
        overview=detail['overview']
        data={'title':ko_title,'poster':poster,'overview':overview}
        details.append(data)
    return details


#초기화면, index.html을 출력해주는 app(먼저 home.html로 이동하고 index.html로 이동함)(title은 home, bottom html에서 {{title}} 시 app.py에서 지정한 이름이 적용됨)
@app.route('/')
def index():
    return render_template('index.html',pageName='home.html',title='영화추천')

@app.route('/overview')
def overview():
    return render_template('index.html',pageName='overview.html',title='줄거리추천')



if __name__=='__main__':
    app.run(port=5000,debug=True)