import win32api
import pyautogui
import time
from random import randint, uniform


def click_spell(x=randint(1153, 1168), y=randint(339, 353)):
    win32api.SetCursorPos((x, y))
    time.sleep(round(uniform(0.1, 0.2), 2))
    pyautogui.click(clicks=1, interval=(round(uniform(0.02, 0.05), 2)))
    time.sleep(round(uniform(0.07, 0.10), 2))
