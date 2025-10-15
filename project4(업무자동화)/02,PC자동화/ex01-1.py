#마우스 커서를 자동으로 조정하는 함수
import pyautogui

# Point(x=1709, y=153) 마우스 커서 위치를 출력 (아이콘의 위치를 찾는데 사용)
# pyautogui.sleep(2)
# p=pyautogui.position()
# print(p) 


#마우스 커서 위치를 이동함(duration은 마우스가 2초에 걸쳐 천천히 이동함) #클릭위치조정
# pyautogui.sleep(2)
# a=pyautogui.moveTo(1828,61,duration=2) 
# pyautogui.click(a) 

#_____________________위 내용 주석화 후 진행
#마우스에 대한 정보 제공
pyautogui.mouseInfo() 
pyautogui.sleep(2)
#마우스의 현재위치
print(pyautogui.position(1)) 

pyautogui.moveTo(500,500, duration=0.5)
pyautogui.move(100,100,duration=0.5)
pyautogui.move(100,100,duration=0.5)