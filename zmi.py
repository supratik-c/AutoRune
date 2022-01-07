from subprocess import run
import numpy as np
import pyautogui as pg
import clicker as ck
import time


def craft_runes():
    ck.move(1847, 1269, spread = 1)
    pg.leftClick()
    time.sleep(30)

def run_to_bank():
    ck.move(728, 175, spread = 0)
    pg.leftClick()
    time.sleep(30)
    ck.move(1260, 700, spread = 0, speed = 0.2)
    pg.leftClick()
    time.sleep(1)

def deposit_runes():
    for col in range(1, 5):
        for row in range(1, 5):

            # Skip Mind Runes
            if col == 1 and row  == 1:
                continue

            x, y = ck.inventory(col, row)
            ck.move(x, y, speed = 0.1, movement = "simple")
            pg.leftClick()

def withdraw_essence():
    x, y = ck.bank(1, 1)
    ck.move(x, y)
    pg.leftClick()

def eat_food():
    bank_x, bank_y = ck.bank(3, 1)
    inv_x, inv_y = ck.inventory(2, 1)

    ck.move(bank_x, bank_y)
    ck.select(2)
    ck.move(inv_x, inv_y)
    ck.select(8)

def drink_stamina():
    bank_x, bank_y = ck.bank(2, 1)
    inv_x, inv_y = ck.inventory(2, 1)

    ck.move(bank_x, bank_y)
    ck.select(2)
    ck.move(inv_x, inv_y)
    ck.select(8)




# Event Loop
for i in range(1):
    
    # Drink potion and eat food every other run
    if i % 2 == 0:
        eat_food()
        drink_stamina()
    
    # Rune Run
    withdraw_essence()
    craft_runes()
    run_to_bank()
    deposit_runes()





