import pyautogui
import random
import time

def move_pointer():
    x = random.randint(0,500)
    y = random.randint(0,500)
    pyautogui.moveTo(501 - x, 500 -  y, duration=1)


pyautogui.moveTo(500, 500, duration=1)
while True:
    time.sleep(4)
    move_pointer()


