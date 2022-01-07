import numpy as np
import pyautogui as pg
import clicker as ck
import time

"""
Start at hosidius bank. Orient Camera West
"""

# Co-ordinates
bank_walk_x, bank_walk_y = 2364, 142
chest_x, chest_y = 1227, 482
karam_x, karam_y = ck.bank(2, 1)
range_walk_x, range_walk_y = 2434, 157
range_x, range_y = 1658, 768
inv_x, inv_y = ck.inventory(4, 7)

# Event Loop
for i in range(2):

    # Withdraw karambwans
    ck.move(chest_x, chest_y)
    pg.leftClick()
    ck.deposit_all()
    ck.withdraw(2, 1)

    # Walk to Range
    ck.move(range_walk_x, range_walk_y, spread = 0)
    pg.leftClick()
    time.sleep(2.8)

    # Cook
    for i in range(36):
        with pg.hold("space"):
            ck.move(inv_x, inv_y, movement = "simple", speed = 0.1)
            pg.leftClick()
            ck.move(range_x, range_y, movement = "simple", speed = 0.1)
            pg.leftClick()


    # Walk to Bank and Deposit
    ck.move(bank_walk_x, bank_walk_y, spread = 0)
    pg.leftClick()
    time.sleep(2.8)
    



