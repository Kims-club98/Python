#이미지를 찾아서 드래그 해주기

import pyautogui

pyautogui.sleep(2)

try:
    manage=pyautogui.locateOnScreen('data/manage.png')
    print(manage)
    pyautogui.click(manage)
    print('클릭 완료')
except Exception:
    print('확인 불가')