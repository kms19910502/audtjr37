import pyautogui
import keyboard
import time






# while 1:
#     pyautogui.click(x=1250,y=1004)
#     time.sleep(0.1)
#     pyautogui.doubleClick(x=1250,y=1004)
#     time.sleep(0.1)

#     if keyboard.is_pressed('f12'):
#         break


while 1:
    pyautogui.press('f5', interval=3)
    print('Do it')
    
    pyautogui.click(x=600,y=400, interval=0.1)
    pyautogui.click(x=700,y=300, interval=0.1)
    pyautogui.click(x=800,y=500, interval=0.1)

    if keyboard.is_pressed('f12'):
        break