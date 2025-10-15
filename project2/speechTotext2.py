import speech_recognition as sr
import os 

def listen(recognizer, audio):
#오류 검증하기
    try: #잘 작동할 때
        text=recognizer.recognize_google(audio,language='ko')
        if "종료" in text: #text에 종료라는 말이 있을 때 Stop하기
            print('종료')
            stop(wait_for_stop=True)
            os.exit(0)
        print("[홍길동]" + text)
    except sr.UnknownValueError: #인식되지 않았을 떄
        print('인식실패')
    except sr.RequestError: #요청된 사항이 실패했을 때
        print('요청실패')

print('말씀하세요!')
#마이크 만들기
mic=sr.Microphone()

#backgroud에서 계속 듣기
stop=sr.Recognizer().listen_in_background(mic,listen)

#무한반복 실행
while True:
    pass
