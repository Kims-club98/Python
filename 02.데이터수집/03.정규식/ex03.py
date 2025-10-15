#정규식
import re

pattern = re.compile('se$') # se로 긑나는가? # case / sece
while True:
    word=input('단어>')
    if word=='':break

    match=pattern.search(word)
    if match:
        print('일치')
    else:
        print('불일치')

# ^ 특정 문자로 시작 ^00
# $ 특정 문자로 끝 00$
# . 중간글자 00.0