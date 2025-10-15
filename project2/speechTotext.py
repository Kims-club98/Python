import speech_recognition as sr

r=sr.Recognizer()
with sr.Microphone() as source:
    print('듣는중...')
    audio=sr.Recognizer().listen(source)

text=sr.Recognizer().recognize_google(audio,language='ko')
print(text)
