from flask import Flask, render_template,request, session #session면 어느 서버에서 연결 가능
from flask_socketio import SocketIO,emit,leave_room,join_room

app=Flask(__name__, template_folder='temp')
app.secret_key='1234'
socketio=SocketIO(app)

#일반적으로 시작페이지를 index로 만듦(index는 html로 만듦)
@app.route('/')
def index():
    return render_template('index.html',title='HOME',PageName='home.html')

# 채팅방마다 지정(친구 0, 가족 1 직장 2 번 지정)
@app.route('/chat/<room>')
def chat(room):
    uid=request.args.get('uid')
    room_names=['친구','가족','회사']
    session['uid']=uid
    session['room']=room
    room_name=room_names[int(room)] #0,1,2을 받아서 room_names의 배열에 넣어줌, 그리고 이를 내보냄
    return render_template('index.html',title='채팅방',PageName='chat.html', room=room_name,uid=uid)

@socketio.on("joined", namespace='/chat')
def joined():
    uid=session['uid']
    room=session['room']
    join_room(room)
    msg=f'{uid}님이 입장'
    emit('status',{'msg':msg}, room=room)

@socketio.on("text", namespace='/chat')
def text(data):
    uid=session['uid']
    room=session['room']
    msg=data.get('msg')
    emit("message",{'msg':f'{uid}:{msg}'},room=room)

@socketio.on("left",namespace='/chat')
def left():
    uid=session['uid']
    msg=f'{uid}님이 퇴장하였습니다.'
    room=session['room']
    emit("status",{'msg':msg}, room=room)
    leave_room(room)

if __name__=='__main__':
    # app.run(port=5000,debug=True)
     socketio.run(app, host='0.0.0.0', port=5000, debug=False)