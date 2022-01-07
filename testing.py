import clicker as ck
import time
import numpy as np
import pyautogui as pg

bank_x, bank_y = ck.bank(2, 1)
inv_x, inv_y = ck.inventory(2, 1)

ck.move(bank_x, bank_y)
ck.select(2)
ck.move(inv_x, inv_y)
ck.select(8)
