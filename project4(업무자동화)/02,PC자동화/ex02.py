#윈도우 조정하기
import pyautogui
import pygetwindow

# pyautogui.sleep(2)
# aw=pyautogui.getActiveWindow()
# print(aw,title)
# print(aw,size)

# aw=pygetwindow.getActiveWindow()
# #매뉴 위치로 이동
# pyautogui.moveTo(aw.left+100,aw.top+100,duration=1)

#지금 띄워진 창에 대한 위치정보(커서위치) 제공
# for w in pygetwindow.getAllWindows():
#     print(w)

#'제목 없음'이라는 이름의 파일의 위치를 찾음
windows=pygetwindow.getWindowsWithTitle('제목 없음')
for w in windows:
    print(w)

#제목 없음 윈도우중 첫번쨰를 활성화시킴
w1=windows[0]
if w1.isActive==False:
    w1.activate()

# 첫 번째 위도우를 최대화
pyautogui.sleep(1)
if w1.isMaximized == False:
    w1.maximize()

# 첫 번째 위도우를 최소화
pyautogui.sleep(1)
if w1.isMinimized==False:
    w1.minimize()
