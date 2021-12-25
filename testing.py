import clicker as ck
import time
import numpy as np
import pyautogui as pg

for i in range(20):
    rands = np.random.uniform(1, 10, 1000)
    greaters = rands[rands > 9.33]
    print(len(greaters))