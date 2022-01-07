import numpy as np
import pyautogui as pg
import clicker as ck
import time

for i in range(400):
    
    # Click fishing spot
    ck.move(1319, 1330)
    pg.leftClick()
    time.sleep(90)

    # Drop Fish
    for row in range(2, 8):
        for col in range(1, 5):
            inv_x, inv_y = ck.inventory(col, row)
            ck.move(inv_x, inv_y, speed = 0.1)
            pg.leftClick()
