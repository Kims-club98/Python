#메모장을 드레그 하기
import pyautogui

# pyautogui.sleep(2)
# print(pyautogui.position()) 
# 메모장 창 위치Point(x=1369, y=195)

# moveto는 절대적 위치, move는 상대적 위치
pyautogui.sleep(2)
p=pyautogui.position()
pyautogui.click(p.x,p.y,duration=0.5)

pyautogui.moveTo(p.x,p.y,duration=1)
pyautogui.drag(100,100,duration=1)