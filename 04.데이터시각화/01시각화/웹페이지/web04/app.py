from flask import Flask, render_template, request,send_file
import pandas as pd #데이터를 가져오기 위해서 pandas를 가지고 옴


app=Flask(__name__,template_folder='Temp')

@app.route('/score') #출력을 위한 라우터
def score():
    return render_template('score.html') #/stu를 입력하면 위 Temp 폴더에 있는 stu.html이 열림

@app.route('/score/data') #데이터를 가지고 와주는 라우터
def score_data():
    word=request.args["word"]
    df = pd.read_csv(f'{app.root_path}/static/score.csv')
    df['평균'] = df[['국어','영어','수학','과학','사회']].mean(axis=1)
    filt = (df['이름'].str.contains(word)) | (df['학교'].str.contains(word))
    df = df[filt]
    df_info=df[['지원번호','이름','학교','키','SW특기']]
    df_score=df[['지원번호','이름','국어','영어','수학','과학','사회']]
    
    table_info=df_info.to_html(classes="table table-striped table-hover", index=False)
    table_score=df_score.to_html(classes="table table-striped table-hover", index=False)
    data={'info': table_info, 'score':table_score}
    return data

@app.route('/score/graph')
def score_graph():
        import matplotlib.pyplot as plt
        from io import BytesIO
        plt.rc('font',family='Malgun Gothic') # 폰트 선택ㅇ
        plt.rc('font',size=11) #폰트크기 11
        plt.rc('axes',unicode_minus=False) #한글 깨짐 방지
        
        df=pd.read_csv(f'{app.root_path}/static/score.csv')
        df['평균'] = df[['국어','영어','수학','과학','사회']].mean(axis=1)
        plt.bar(df['이름'],df['평균'])

        img=BytesIO()
        plt.savefig(img, format='png')
        plt.close()
        img.seek(0)
        return send_file(img, mimetype='image/png')

if __name__=='__main__':
    app.run(port=5000,debug=True)