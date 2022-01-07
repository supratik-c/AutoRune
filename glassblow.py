import numpy as np
import pyautogui as pg
import clicker as ck
import time

pipe_x, pipe_y = ck.inventory(1, 1)
glass_x, glass_y = ck.inventory(2, 1)
banker_x, banker_y = (958, 691)

for i in range(11):
    
    # Withdraw glass
    ck.withdraw(2, 1)
    ck.close_bank()
    
    # Craft and Wait
    ck.move(pipe_x, pipe_y)
    pg.leftClick()
    ck.move(glass_x, glass_y)
    pg.leftClick()
    time.sleep(1)
    pg.press("space")
    time.sleep(50)

    # Deposit Glass
    ck.move(banker_x, banker_y)
    pg.leftClick()
    ck.move(glass_x, glass_y)
    ck.select(6)


