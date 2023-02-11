import pyautogui, webbrowser
from time import sleep

webbrowser.open('http://web.whatsapp.com/send?phone=+57')

sleep(30)

with open('song.txt', 'r') as file:
    for line in file:
        pyautogui.typewrite(line)
        pyautogui.press("enter")