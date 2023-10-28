import pyautogui
import time
import random

screenWidth, screenHeight = pyautogui.size()
print(screenWidth, screenHeight)
screenHeight -= 5

time.sleep(2)

def blowLine(speed):
    width = 0
    for i in range(1, 7):
        pyautogui.moveTo(width, 1)
        pyautogui.moveRel(0, screenHeight, duration = speed)
        width += screenWidth/5
        if width > screenWidth:
            width = 0

def blowRandom(speed):
    for i in range(1, 40):
        pyautogui.moveTo(random.randint(1, screenWidth), random.randint(1, screenHeight), duration = speed)

def run(speed):
    blowLine(speed)
    blowRandom(speed)

while True:
    run(1)