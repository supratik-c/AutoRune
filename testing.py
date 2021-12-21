import clicker as ck
import time
import numpy as np
import pyautogui as pg

inv_x, inv_y = ck.inventory(2, 1)

ck.move(inv_x, inv_y)
pg.rightClick(duration = 0.3)
pg.leftClick(duration = 0.3)
with pg.hold("shift"):
    pg.leftClick(duration = 0.1)
    time.sleep(0.8)

