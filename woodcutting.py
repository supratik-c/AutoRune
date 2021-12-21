import numpy as np
import pyautogui as pg
import clicker as ck
import time
import keyboard as kb

# Co-ordinates
left_x, left_y = 885, 835
right_x, right_y = 1565, 869

for i in range(100):

    # Cut trees
    for i in range(5):

        # Chop left tree
        ck.move(left_x, left_y)
        pg.leftClick()
        time.sleep(np.random.normal(25, 2))

        # Chop right tree
        ck.move(right_x, right_y)
        pg.leftClick()
        time.sleep(np.random.normal(25, 2))
    
    
    # Inventory management
    for col in range(1, 5):
        for row in range(1, 8):

            # Skip axes
            if row == 1 and col == 1:
                continue

            if row == 1 and col == 2:
                continue
            
            # Drop logs
            inv_x, inv_y = ck.inventory(col, row)
            ck.move(inv_x, inv_y, speed = 0.2)
            time.sleep(np.random.uniform(0.3, 0.6))
            
            if row == 7:
                ck.select(1)
            else:
                ck.select(2)
            