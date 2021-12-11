import clicker as ck
import time
import numpy as np
import pyautogui as pg

# Smelter-to-Bank
bank_x = 680
bank_y = 981

# Move to Bank
with pg.hold("control"):
    ck.move(1280, 720)
    time.sleep(np.random.uniform(0.5, 1)) 
    pg.leftClick()
    pg.rightClick()

