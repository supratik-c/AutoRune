import numpy as np
import pyautogui as pg
import clicker as ck
import time
import keyboard as kb

for i in range(10000):
    
    # Mine Ores
    for i in range(14):
        ck.move(1536, 745)
        pg.leftClick()
        time.sleep(15)
        ck.move(925, 751)
        pg.leftClick()
        time.sleep(15)
    
    # Drop Ores
    for col in range(1, 5):
        for row in range(1, 8):

            inv_x, inv_y = ck.inventory(col, row)
            ck.move(inv_x, inv_y, speed = 0.2)
            ck.drop()