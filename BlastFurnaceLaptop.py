import numpy as np
import pyautogui as pg
import clicker as ck
import time
import keyboard as kb
from datetime import datetime as dt
import datetime

"""
Start in front of the bank at Blast Furnace on a BF world. Orient North. Max zoom out. Rotate camera upwards maximally.
Have coins in slot 1 inventory, coal in slot 2 bank, iron in slot 3 bank and 1-dose stamina potions in slot 4 bank. Have bank interface open.
Run.
"""

def close_bank():
    ck.move(1415, 54)
    pg.leftClick()


def deposit(coins: str) -> None:
    
    # Close Bank
    close_bank()


    # Click Coffer
    ck.move(1178, 704, speed = 0.3, spread = 0)
    pg.leftClick()
    time.sleep(np.random.uniform(1.5, 1.75))


    # Deposit Coins
    pg.press("1")
    time.sleep(1.5)
    for i in coins:
        pg.typewrite(i, interval = np.random.uniform(0.2, 0.25))
    pg.press("return")


    # Deposit All Coins
    ck.move(1300, 744, speed = 0.3)
    pg.leftClick()
    deposit_x, deposit_y = (1346, 1121)
    ck.move(deposit_x, deposit_y, speed = 0.8)
    pg.leftClick()
    time.sleep(np.random.uniform(0.5, 1))
    deposit_all()


def withdraw_coal() -> None:
    coal_x, coal_y = ck.bank(2, 1)
    ck.move(coal_x, coal_y, speed = 0.5)
    ck.select(6)
    

def withdraw_iron() -> None:
    iron_x, iron_y = ck.bank(3, 1)
    ck.move(iron_x, iron_y, speed = 0.5)
    ck.select(6)


def deposit_all():
    deposit_x, deposit_y = (1346, 1121)
    ck.move(deposit_x, deposit_y, speed = 0.6)
    pg.leftClick()


def drink_stamina():
    
    # Withdraw potion
    stam_x, stam_y = ck.bank(4, 1)
    ck.move(stam_x, stam_y, speed = 0.5)
    pg.leftClick()

    # Drink from inventory
    inv_x, inv_y = ck.inventory(1, 1)
    ck.move(inv_x, inv_y)
    ck.select(7)


def bank_to_belt():
    close_bank()
    belt_x, belt_y = (1069, 334)
    ck.move(belt_x, belt_y)
    pg.leftClick()
    time.sleep(7)


def belt_to_bank():
    bank_x, bank_y = (1572, 1251)
    ck.move(bank_x, bank_y)
    pg.leftClick()
    time.sleep(7)


def collect_bars():
    
    # Move to the dispenser
    bars_x, bars_y = (1138, 888)
    ck.move(bars_x, bars_y)
    pg.leftClick()
    time.sleep(4.8)

    # Collect from dispenser
    disp_x, disp_y = (1311, 705)
    ck.move(disp_x, disp_y, spread = 0)
    pg.leftClick()
    time.sleep(1)
    pg.press("space")

    # Run to bank
    bank_x, bank_y = (1731, 1044)
    ck.move(bank_x, bank_y)
    pg.leftClick()
    time.sleep(4)
    deposit_all()

def bank_to_bars():
    deposit_all()
    close_bank()
    ck.move(947, 483, spread = 0)
    pg.leftClick()
    time.sleep(4)
    pg.press("space")
    ck.move(1605, 975)
    pg.leftClick()
    time.sleep(4)
    deposit_all()

def main(n: str):

    # Setup
    coins_required = n * 1050
    deposit(str(coins_required))
    start = dt.now()
    drink_stamina()

    # Main event loop
    for i in range(n):

        # Every 10 runs do a bar collection - RNG protection
        if np.random.uniform(0, 10) > 8.5:
            bank_to_bars()

        
        # Decide if potion needs to be drunk
        now = dt.now()
        diff = (now - start).total_seconds()
        if diff > 95:
            drink_stamina()
            start = dt.now()
    
        
        # Run Coal
        withdraw_coal()
        bank_to_belt()
        belt_to_bank()

        # Run Iron and Collect Bars
        withdraw_iron()
        bank_to_belt()
        collect_bars()


if __name__ == "__main__":
    main(28)