from flask import Flask, render_template,request, session #session면 어느 서버에서 연결 가능
from flask_socketio import SocketIO,emit,leave_room,join_room
from scrapping import answer
from gtts import gTTS
from playsound import playsound
import os

app=Flask(__name__, template_folder='temp')
app.secret_key='1234'
socketio=SocketIO(app)

#목소리 tts
def speak():
    file_name='voice.mp3'
    tts=gTTS(text=text,lang='ko')
    tts.save(file_name)
    playsound(file_name)
    if os.path.exists(file_name):
        os.remove(file_name)

#일반적으로 시작페이지를 index로 만듦(index는 html로 만듦)
@app.route('/')
def index():
    return render_template('index.html',title='HOME',PageName='home.html')


@app.route('/chat/<uid>')
def chat(uid):
    session['uid']=uid
    session['room']=uid
    return render_template('index.html',title='채팅방',PageName='chat.html', room='인공지능',uid=uid)

@socketio.on("joined", namespace='/chat')
def joined():
    uid=session['uid']
    room=session['room']
    join_room(room)
    msg=f'{uid}님 입장하셨습니다.'
    emit('status',{'msg':msg}, room=room)

@socketio.on("text", namespace='/chat')
def text(data):
    uid=session['uid']
    room=session['room']
    msg=data.get('msg')
    #내가 질문한 메시지 & 인공지능이 답한 메시지
    emit("message",{'msg':f'{uid}:{msg}'},room=room)
    answer_text=answer(msg)
    emit('message',{'msg':f'인공지능: {answer_text}'},room=room)
    speak(answer_text)
   

@socketio.on("left",namespace='/chat')
def left():
    uid=session['uid']
    msg=f'{uid}님이 퇴장하였습니다.'
    room=session['room']
    emit("status",{'msg':msg}, room=room)
    leave_room(room)

if __name__=='__main__':
    app.run(port=5000,debug=True)