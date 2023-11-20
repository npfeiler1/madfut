import sys
import pyautogui
import time
import keyboard

walkouts = '0'
time.sleep(5)

def quit():
    if keyboard.is_pressed('q'):
        print(walkouts)
        sys.exit()

def colorChange(x: int, y: int, time: int) -> bool:

    initial_color = pyautogui.pixel(x, y)
    time.sleep(time)
    current_color = pyautogui.pixel(x, y)
    if current_color != initial_color: return True

def click(clickX: int, clickY: int, time: int) -> None:

    pyautogui.click(clickX, clickY)
    time.sleep(time)

if __name__ == "__main__":
    while True:
        click(1923, 992, 1)
        click(1923, 992, 2)
        click(1923, 1580, 0)

        if colorChange(1790, 480, 1):
            time.sleep(3)
            click(2385, 187, 3)
            walkouts = walkouts +1
        else:
            pyautogui.click(1923, 1580, 4.5)

    click(1923, 2018, 2)



