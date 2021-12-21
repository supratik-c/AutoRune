import numpy as np
import pyautogui as pg
import clicker as ck
import time
import keyboard as kb


ck.move(2448, 1102)
pg.leftClick()
time.sleep(0.6)


for i in range(3023):
    pg.leftClick()
    time.sleep(np.random.normal(1.6, 0.1))
