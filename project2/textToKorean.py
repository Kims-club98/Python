from gtts import gTTS
from playsound import playsound

file_name='data/sample2.mp3'
text='안녕하세요'
tts_ko=gTTS(text=text, lang='ko')
tts_ko.save(file_name)
playsound(file_name)