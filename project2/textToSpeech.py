from gtts import gTTS
from playsound import playsound

#텍스트를 저장할 파일명
file_name="data/sample.mp3"
#tts 받을 텍스트
text= "Can i help you?"
tts_en=gTTS(text=text,lang='en')
tts_en.save(file_name)
playsound(file_name)
