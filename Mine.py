import pyautogui as pg
import time
import mouse as m
from ctypes import *
import random
import keyboard as kb

def clearScreen():
    pg.moveRel(0, 300, .1)
    pg.leftClick()

def crank():
    pg.press('z')
    kb.press('e')
    time.sleep(.5)
    kb.release('e')
    
    time.sleep(.2)
    pg.press('x')
    time.sleep(.1)
    kb.press('e')
    time.sleep(.1)
    kb.release('e')
    time.sleep(.1)
    pg.press('space')
    pg.press('c')
    kb.press('e')
    time.sleep(.1)
    kb.release('e')
    
    



clearScreen()
time.sleep(.5)
crank()
