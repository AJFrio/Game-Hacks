import pyautogui
import time

time.sleep(2)

#print(pyautogui.position())

pyautogui.click(821, 653)


def lasers():
    for i in range(1, 11):
        pyautogui.mouseDown(button='right')
        pyautogui.mouseUp(button='right')

def bomb():
    pyautogui.typewrite(["space"])

def play():
    for i in range(1, 100000):
        bomb()
        lasers()
        bomb()
        time.sleep(.5)
        pyautogui.click(821, 653)
    

play()