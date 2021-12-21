import numpy as np
import pyautogui as pg
import clicker as ck
import time
import keyboard as kb

"""
Start at Al Kharid three-iron mining spot. Orient camera West and zoom in max.
"""


# Co-ordinates
sr_x, sr_y = 964, 791
wr_x, wr_y = 1303, 454
nr_x, nr_y = 1618, 783
inv_x, inv_y = ck.inventory(1, 1)
gem_x, gem_y = ck.inventory(2, 1)


# Event loop
for i in range(10000):
    
    # Mine Southern Rock
    ck.move(sr_x, sr_y)
    time.sleep(np.random.uniform(0.2, 0.5))
    pg.leftClick()
    ck.move(inv_x, inv_y)
    time.sleep(np.random.uniform(1.5, 2))
    ck.select(2)

        # Drop gem
    if np.random.uniform(1, 50) < 5:
        ck.move(gem_x, gem_y)
        time.sleep(np.random.uniform(0.2, 0.5))
        ck.select(2)


    # Mine Western Rock
    ck.move(wr_x, wr_y)
    time.sleep(np.random.uniform(0.2, 0.5))
    pg.leftClick()
    ck.move(inv_x, inv_y)
    time.sleep(np.random.uniform(1.5, 2))
    ck.select(2)

        # Drop gem
    if np.random.uniform(1, 50) < 5:
        ck.move(gem_x, gem_y)
        time.sleep(np.random.uniform(0.2, 0.5))
        ck.select(2)


    # Mine Northern Rock
    ck.move(nr_x, nr_y)
    time.sleep(np.random.uniform(0.2, 0.5))
    pg.leftClick()
    ck.move(inv_x, inv_y)
    time.sleep(np.random.uniform(1.5, 2))
    ck.select(2)

    # Drop gem
    if np.random.uniform(1, 50) < 8:
        ck.move(gem_x, gem_y)
        time.sleep(np.random.uniform(0.2, 0.5))
        ck.select(2)






