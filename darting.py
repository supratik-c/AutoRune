import numpy as np
import pyautogui as pg
import clicker as ck
import time
import keyboard as kb

# Co-ordinates
tip_x, tip_y = ck.inventory(4, 7)
feather_x, feather_y = ck.inventory(3, 7)


for i in range(781):
    ck.move(tip_x, tip_y, 0.1, movement = "simple")
    pg.leftClick()
    ck.move(feather_x, feather_y, 0.1, movement = "simple")
    pg.leftClick()
