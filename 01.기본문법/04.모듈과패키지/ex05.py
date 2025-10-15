#패키지 만들기
import os

path = os.getcwd()
print("현재폴더",path) #작업위치 찾기

check = path + '/04.모듈과패키지/travel'
if os.path.exists(check): #새로 삭제 rmdir
    os.rmdir(check)
    print('폴더삭제')
else:
    os.makedirs(check) #새로 생성 makedirs
    print('폴더생성')
