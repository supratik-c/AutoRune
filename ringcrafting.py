import numpy as np
import pyautogui as pg
import clicker as ck
import time
import keyboard as kb

"""
This script will auto make rings at Edgeville. Keep gold bars in the second bank slot, and jewellery in the third.
Make sure you have a ring mould in inventory. Start at the furnace, orient north, zoom out max, move camera upwards to max, and run.
"""

# Smelter-to-Bank
bank_x, bank_y = ck.normalize(680, 981)

# Bank-to-Smelter
smelter_x, smelter_y = ck.normalize(1742, 527)

# Run co-ordinates
run_x, run_y = ck.normalize(2282, 216)

# Rings inventory co-ordinates
rx, ry = ck.inventory(2, 1)

# Gold Bars bank co-ordinates
gbx, gby = ck.bank(2, 1)

# Emerald bank co-ordinates
ex, ey = ck.bank(3, 1)

# Emerald crafting co-ordinates
cx, cy = ck.normalize(920, 485)


# Event loop - Start at Smelter
for i in range(118):

    # Turn on Run
    ck.move(run_x, run_y)
    time.sleep(np.random.uniform(0.3, 0.7))
    pg.leftClick()

    # Move to Bank
    ck.move(bank_x, bank_y, spread = 2)
    time.sleep(np.random.uniform(0.5, 1)) 
    pg.leftClick()
    time.sleep(12 + np.random.normal(1, 0.4))

    # Deposit Rings
    ck.move(rx, ry)
    time.sleep(np.random.uniform(0.5, 1)) 
    ck.select(6)

    # Withdraw Gold Bars
    ck.move(gbx, gby)
    time.sleep(np.random.uniform(0.5, 1)) 
    ck.select(4)

    # Withdraw Emeralds
    ck.move(ex, ey)
    time.sleep(np.random.uniform(0.5, 1)) 
    ck.select(4)

    # Turn off Run
    ck.move(run_x, run_y)
    time.sleep(np.random.uniform(0.3, 0.7))
    pg.leftClick()

    # Move to Smelter
    ck.move(smelter_x, smelter_y, spread = 3)
    time.sleep(np.random.uniform(0.5, 1))
    ck.select(0)
    time.sleep(14 + np.random.normal(1, 0.4))
    ck.move(cx, cy)
    time.sleep(np.random.uniform(0.5, 1))
    ck.select(0)
    time.sleep(22 + np.random.uniform(1, 10))