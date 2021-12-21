import numpy as np
import pyautogui as pg
import clicker as ck
import time
import keyboard as kb

# Co-ordinates
bank_x, bank_y = ck.normalize(1057, 786)
salt_x, salt_y = ck.bank(2, 1)
fert_x, fert_y = ck.bank(3, 1)
close_x, close_y = ck.normalize(1415, 54)
deposit_x, deposit_y = (1346, 1121)


for i in range(35):

    # Withdraw
    for i in range(7):
        ck.move(salt_x, salt_y, 0.05, movement = "simple")
        ck.select(0)
        ck.select(0)
        ck.move(fert_x, fert_y, 0.05, movement = "simple")
        ck.select(0)
        ck.select(0)
    
    # Close Bank
    ck.move(close_x, close_y)
    pg.leftClick()

    # Make Loop
    for col in range(1, 3):
        for row in range(1, 8):
            inv_salt_x, inv_salt_y = ck.inventory(col, row)
            inv_fert_x, inv_fert_y = ck.inventory(col + 2, row)

            ck.move(inv_salt_x, inv_salt_y, 0.1, movement = "simple")
            pg.leftClick()
            ck.move(inv_fert_x, inv_fert_y, 0.1, movement = "simple")
            pg.leftClick()
    
    # Deposit
    ck.move(bank_x, bank_y)
    pg.leftClick()
    ck.move(deposit_x, deposit_y)
    pg.leftClick()








