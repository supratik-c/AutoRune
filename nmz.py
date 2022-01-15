import numpy as np
import pyautogui as pg
import clicker as ck
import time



for i in range(10000):
    ck.move(2266, 167)
    pg.doubleClick(interval=0.6)
    time.sleep(0.1)
    
    if i % 20 == 0:
        for row in range(2, 8):
            for col in range(1, 5):
                inv_x, inv_y = ck.inventory(col, row)
                ck.move(inv_x, inv_y, speed = 0.1)
                pg.leftClick()
    
    time.sleep(30)