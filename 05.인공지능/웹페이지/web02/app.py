from flask import Flask, render_template
from routes import linear,multi

app=Flask(__name__, template_folder='temp')
app.register_blueprint(linear.bp)
app.register_blueprint(multi.bp)

#초기화면, index.html을 출력해주는 app(먼저 home.html로 이동하고 index.html로 이동함)(title은 home, bottom html에서 {{title}} 시 app.py에서 지정한 이름이 적용됨)
@app.route('/')
def index():
    return render_template('index.html',pageName='home.html',title='자기소개')

if __name__=='__main__':
    app.run(port=5000,debug=True)