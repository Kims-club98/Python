import os
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import speech_recognition as sr
from answer import weather, exchage,stock #날씨 텍스트에 오늘날씨 tts 해줌(asnwer.py 에서 가져옴)

#문자를 소리로 출력하기(gtts 활용)
def speak(text): #text를 받아야 함
    print('[인공지능]' + text)
    text=gTTS(text=text, lang='ko') #gtts는 lang
    file_name='data/voice.mp3'
    text.save(file_name)
    playsound(file_name)
    #mp3파일을 말하고 바로 삭제하기 위한 기능(speak 이후 바로 삭제됨)
    if os.path.exists(file_name):
        os.remove(file_name)


#음성을 듣고 문자로 출력해주는 함수(recognizer 활용)
def listen(recognizer, audio):
#오류 검증하기
    try: #잘 작동할 때
        text=recognizer.recognize_google(audio,language='ko') #recognize은 language
        answer(text)
    except sr.UnknownValueError: #인식되지 않았을 떄
        print('인식실패')
    except sr.RequestError: #요청된 사항이 실패했을 때
        print('요청실패')

# 문자를 입력받아서 인공지능이 대답을 함
def answer(text):
    answer_text=''
    if '종료' in text:
        answer_text='씨유 넥스트 어 타임'
        speak(answer_text)
        stop(wait_for_stop=False)
        os._exit(0)
    elif '날씨' in text:
        index=text.find('날씨')
        query=text[:index+2]
        temp=weather(query)
        answer_text=f'{query}의 현재 {temp}입니다.'
    elif '환율' in text:
        answer_text='1달러 환율은'+round(exchage(),0)+'원 입니다.' #안돼면 round빼기 #exchage()를 따로 변수지정해도 됨
    elif '주식' in text:
        index=text.find('주식')
        query=text[:index+2]
        price=stock(query)
        answer_text=f'{query}의 현재 가격은 {price}원 입니다.'
    elif '안녕' in text:
        answer_text='안녕하세유 반가워유'
        speak(answer_text)
    else:
        answer_text='인식실패'
    speak(answer_text)


speak('뭘 도와 드릴까?')
#마이크 만들기
mic=sr.Microphone()

#backgroud에서 계속 듣기
stop=sr.Recognizer().listen_in_background(mic,listen)

# 계속 반복해야 하기 때문에 while true가 필요함
while True:
    pass
