from gtts import gTTS
from playsound import playsound

#파일명 지정
file_name='data/sample3.mp3'
#열 파일, 읽기모드, 인코딩해줌
#텍스트파일을 읽기
with open('data/sample_en.txt', 'r', encoding='utf-8') as file:
    text=file.read()
print(text)

tts_en=gTTS(text=text, lang='en')
tts_en.save(file_name)
playsound(file_name)
