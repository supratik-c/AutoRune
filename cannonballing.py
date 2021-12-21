import numpy as np
import pyautogui as pg
import clicker as ck
import time
import keyboard as kb

"""
This script will auto make cannonballs at Edgeville. Kweep Steel Bars in the second bank slot.
Start at the furnace, orient north, zoom out max, move camera upwards to max, and run.
"""


# Normalize pixel ratio
screenWidth, screenHeight = pg.size()

# Smelter-to-Bank
bank_x = (680 * screenWidth)/ 2560
bank_y = (981 * screenHeight)/ 1440

# Bank-to-Smelter
smelter_x = (1742 * screenWidth)/ 2560
smelter_y = (527 * screenHeight)/ 1440

# Cannonballs inventory co-ordinates
cb_x, cb_y = ck.inventory(2, 1)

# Steel Bars bank co-ordinates
sb_x, sb_y = ck.bank(2, 1)


# Event loop - Start at Smelter
for i in range(118):

    # Move to Bank
    ck.move(bank_x, bank_y, 1, spread = 2)
    time.sleep(1) 
    ck.select(0)
    time.sleep(8 + np.random.normal(1, 0.4))

    # Deposit Cannonballs
    ck.move(cb_x, cb_y)
    time.sleep(1)
    ck.select(6)

    # Withdraw Steel Bars
    ck.move(sb_x, sb_y)
    time.sleep(1)
    ck.select(6)

    # Move to Smelter
    ck.move(smelter_x, smelter_y, 1, spread = 3)
    time.sleep(0.6) 
    ck.select(0)
    time.sleep(8 + np.random.normal(1, 0.4))
    kb.press("space")

    # Move mouse around
    for i in range(15):
        rand_x = np.random.uniform(200, 2200)
        rand_y = np.random.uniform(200, 1200)
        ck.move(rand_x, rand_y, 3)
        time.sleep(10)