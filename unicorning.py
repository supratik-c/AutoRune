
import numpy as np
import pyautogui as pg
import clicker as ck
import time
import keyboard as kb

'''
Grinds unicorn horns into unicorn dust. Start at the grand exchange with only a pestle and mortar in the invetory.
Stand next to the south western banker and orient north with maximal zoom in.
'''

# Bank co-ords
banker_x, banker_y = 1119, 521
bank_horn_x, bank_horn_y = ck.bank(2, 1)
close_x, close_y = 1415, 54

# Inventory co-ords
pm_x, pm_y = ck.inventory(4, 7)
dust_x, dust_y = ck.inventory(1, 1)
horn_x, horn_y = ck.inventory(3, 7)


# Event Loop - Start with Bank Window open, Unicorn horns in second slot
for i in range(2):

    # Withdraw horns from bank
    ck.move(bank_horn_x, bank_horn_y)
    time.sleep(np.random.uniform(0.5, 1.5))
    ck.select(6)
    time.sleep(np.random.uniform(0.5, 1.5))
    ck.move(close_x, close_y)
    time.sleep(0.5)
    ck.select(0)

    # Grind horns
    for i in range(27):
        ck.move(pm_x, pm_y, speed = 0.2)
        time.sleep(np.random.uniform(0.01, 0.03))
        ck.select(0)
        ck.move(horn_x, horn_y, speed = 0.2)
        time.sleep(np.random.uniform(0.01, 0.03))
        ck.select(0)

    # Depost dust in bank
    ck.move(banker_x, banker_y, speed = 2, spread = 3)
    time.sleep(np.random.uniform(0.5, 1.5))
    ck.select(0)
    ck.move(dust_x, dust_y)
    time.sleep(np.random.uniform(0.5, 1.5))
    ck.select(6)