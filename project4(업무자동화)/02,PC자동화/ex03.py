import pyautogui
import pygetwindow

#제목없음 windows에 숫자쓰고, 글자/띄어쓰기 등 수행
window=pygetwindow.getWindowsWithTitle('제목 없음')[0]
window.activate()

pyautogui.write('23456')
pyautogui.write(['T','E','S','T','left','left','-','right','right','enter'])
# pyautogui.keyDown()
# pyautogui.press('4')
#shift키를 자동으로 입력해줌
# pyautogui.keyUp('shift')
pyautogui.sleep(0.5)
for i in range(2):
    pyautogui.hotkey('ctrl','a')
    pyautogui.hotkey('ctrl','c')
    pyautogui.hotkey(['right'])
    pyautogui.hotkey('ctrl','v')

window.close()
pyautogui.write('n')
