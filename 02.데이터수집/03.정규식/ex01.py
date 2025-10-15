#정규식
import re

pattern=re.compile('ca.e') # 시작은 ca로 들어가고 마지막은 e가 만족하는가? .은 1글자를 의미
while True:
    word=input('단어>')
    if word=='':break

    match=pattern.match(word)
    if match:
        print('일치')
    else:
        print('불일치')