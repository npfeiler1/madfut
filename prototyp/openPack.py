import pyautogui
import time

pyautogui.mouseDown()
time.sleep(5)
pyautogui.mouseUp()

while True:
    pyautogui.moveTo(1908, 1677)
    pyautogui.click(1908, 1677)
    time.sleep(4)
    pyautogui.click(1908, 1677)
    time.sleep(1)
    pyautogui.moveTo(1909, 2014)
    pyautogui.click(1909, 2014)
    time.sleep(1)

    #du oarsch