import numpy as np
import pyautogui as pg
import clicker as ck
import time
import keyboard as kb

# Co-ordinates
fruit_x, fruit_y = (917, 762)


# Event loop
for i in range(10):
    
    # Steal fruit
    for i in range(27):
        ck.move(fruit_x, fruit_y, 0.1, movement = "simple")
        pg.leftClick()
        time.sleep(np.random.uniform(3.6, 4.0))

    # Drop fruit
    for col in range(1, 5):
        for row in range(1, 8):

            # Skip first slot
            if row == 1 and col == 1:
                continue

            inv_x, inv_y = ck.inventory(col, row)
            ck.move(inv_x, inv_y, 0.05, movement = "simple")
            ck.drop()


