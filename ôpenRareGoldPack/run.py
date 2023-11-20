import sys
import pyautogui
import time
import keyboard
import getpixelcolor as getpixelcolor

time.sleep(5)

while (True):
    pyautogui.click(1923, 992)
    time.sleep(1)
    pyautogui.click(1923, 992)
    time.sleep(2)
    pyautogui.click(1923, 1580)
    time.sleep(4.5)
    pyautogui.click(1923, 1580)
    time.sleep(2)
    pyautogui.click(1923, 2018)
    time.sleep(2)

def quit():
    if keyboard.is_pressed('q'):
        sys.exit()

def click(clickX: int, clickY: int, colorX: int, colorY: int, time: int) -> None:

    initial_color = pyautogui.pixel(colorX, colorY)

    while True:
        current_color = pyautogui.pixel(colorX, colorY)
        if current_color != initial_color:
            pyautogui.click(clickX, clickY)
            break

        time.sleep(0.5)


if __name__ == "__main__":

    click(1923, 992, )
    click(1923, 992)