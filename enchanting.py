import numpy as np
import pyautogui as pg
import clicker as ck
import time
import keyboard as kb

'''
Stand at southwestern banker in Grand exchange. Orient north. Max zoom in. Air Staff equipped and Cosmic Runes in first inventory slot.
Emerald rings in bank slot 4.
'''

# Co-ordinates
bank_x, bank_y = ck.normalize(1000, 784)
withdraw_x, withdraw_y = ck.bank(4, 1)
close_x, close_y = ck.normalize(1415, 54)
spellbook_x, spellbook_y = ck.normalize(2497,  925)
enchant_x, enchant_y = ck.normalize(2304,  1042)
deposit_x, deposit_y = ck.inventory(2, 1)

# Click bank
ck.move(bank_x, bank_y)
time.sleep(np.random.uniform(0.5, 1))
pg.leftClick()

# Event Loop
for i in range(44):

    # Withdraw rings
    ck.move(withdraw_x, withdraw_y)
    time.sleep(np.random.uniform(0.3, 0.8))
    ck.select(6)
    ck.move(close_x, close_y)
    time.sleep(np.random.uniform(0.2, 0.5))
    pg.leftClick()

    # Iterate through cols and rows of inventory
    for col in range(1, 5):
        for row in range(1, 8):

            # Bank slot
            if row == 1 and col == 1:
                row += 1
            
            inv_x, inv_y = ck.inventory(col, row)

            # Enchant
            ck.move(enchant_x, enchant_y, speed = 0.2)
            time.sleep(np.random.uniform(0.5, 0.7))
            pg.leftClick()
            ck.move(inv_x, inv_y, speed = 0.2)
            time.sleep(np.random.uniform(0.5, 0.7))
            pg.leftClick()
            time.sleep(np.random.uniform(0.5, 0.7))
    
    # Deposit
    ck.move(bank_x, bank_y)
    time.sleep(np.random.uniform(0.5, 1))
    pg.leftClick()
    ck.move(deposit_x, deposit_y)
    time.sleep(np.random.uniform(0.5, 1))
    ck.select(6)