import pyautogui as pg
import random
import time

battle = [989, 641]
card1 = [861, 904]
card2 = [963, 907]
card3 = [1053, 907]
card4 = [1170, 907]
ok = [962, 907]

def grabAndPlace(x, y):
    pg.moveTo(x, y)
    pg.dragTo(x, y-200, duration = .2)

def grabScreen():
    pass

def play():
    pg.click(battle[0], battle[1])

time.sleep(2)
while True:
    play()
    time.sleep(7)
    pg.click(ok[0], ok[1])
    for i in range(40):
        grabAndPlace(card1[0], card1[1])
        grabAndPlace(card2[0], card2[1])
        grabAndPlace(card3[0], card3[1])
        grabAndPlace(card4[0], card4[1])
        time.sleep(random.randint(1, 5))
    time.sleep(10)
    pg.click(ok[0], ok[1])
    time.sleep(7)
