from bot.get_from_bank import click_leather_bank
from bot.make_leather import click_spell
from bot.deposit_to_bank import click_bank, deposit_items
import win32gui
import pyautogui
import time
from random import uniform


def main():
    while True:
        time.sleep(round(uniform(0.08, 0.12), 2))
        click_leather_bank()
        pyautogui.press("esc")
        time.sleep(round(uniform(0.08, 0.12), 2))
        for i in range(5):
            click_spell()
            time.sleep(round(uniform(1.85, 1.95), 2))
        click_bank()
        time.sleep(round(uniform(0.2, 0.3), 2))
        deposit_items()
        time.sleep(round(uniform(0.08, 0.12), 2))


if __name__ == "__main__":
    time.sleep(5)
    main()
