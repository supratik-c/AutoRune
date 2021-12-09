import numpy as np
import pyautogui as pg
import keyboard as kb
import time
import bezier as bz
import random as rd
from datetime import datetime as dt
import os
from dotenv import load_dotenv

# Remove minimums
pg.PAUSE = 0
pg.MINIMUM_DURATION = 0
pg.MINIMUM_SLEEP = 0.005

# Generates Bezier curve
def make_curve(start: tuple, end: tuple) -> bz.Curve:
    '''
    Takes in two tuples representing start and end co-ordinates and generates a bezier curve between them
    '''
    
    # Unpack co-ordinates
    start_x, start_y = start
    end_x, end_y = end
    size = 2
    
    # Generate a random point between co-ords
    mid_x = sorted(np.random.uniform(min(start_x, end_x), max(start_x, end_x), size = size))
    mid_y = sorted(np.random.uniform(min(start_y, end_y), max(start_y, end_y), size = size))

    # Generate Bezier curve
    nodes = np.asarray([
        [start_x] + mid_x + [end_x],
        [start_y] + mid_y + [end_y]
    ])

    curve = bz.Curve(nodes, degree = size + 1)
    return curve


# Move mouse to location
def move(x: int, y: int, speed: float = 1, points: float = 10, spread: int = 3) -> None:
    
    # Normally distribute start & end coords
    curr_x, curr_y = pg.position()
    rand_x = np.random.normal(x, spread) 
    rand_y = np.random.normal(y, spread)

    # Normally distribute speed
    rand_speed = np.random.uniform(0.1, speed) * 0.6 * (1/points)

    # Easing functions for random choice of mouse movement
    tweens = [pg.easeOutBack, pg.easeOutQuad, pg.easeOutCubic, pg.easeOutExpo, pg.easeInQuad, pg.easeInCubic, pg.easeInExpo]
    
    # Generate and split bezier curve
    curve = make_curve((curr_x, curr_y), (rand_x, rand_y))
    curve_points = sorted(np.random.uniform(0.01, 0.99, points)) + [1]
    curve_coords = map(curve.evaluate, curve_points)

    # Move along the curve
    for pos in curve_coords: 
        next_x, next_y = pos
        pg.moveTo(next_x, next_y, rand_speed, tween = (np.random.choice(tweens) if next_x == rand_x and next_y == rand_y else pg.linear))


# Select Option 
def select(option: int) -> None:

    # Screen resolution for scaling
    res_x, res_y = pg.size()
    x_offset = (10 * res_x)/2560
    y_offset = (38 * res_y)/1440
    y_option_offset = (23 * res_y)/1440

    # M1 click
    if option == 0:
        pg.leftClick()
        return

    # M2 Option Select
    pg.rightClick()
    curr_x, curr_y = pg.position()
    rand_x = curr_x + x_offset
    rand_y = curr_y + y_offset + (y_option_offset * (option - 1)) 
    move(rand_x, rand_y, 0.7, spread = 1)
    pg.leftClick()


# Moves to a specific inventory row & column
def inventory(row: int, col: int) -> tuple:
    screenWidth, screenHeight = pg.size()
    base_x, base_y = (2246 * screenWidth)/2560 , (986 * screenHeight)/1440
    offset_x, offset_y = (65 * screenWidth)/2560 , (55 * screenHeight)/1440
    return (base_x + (row - 1) * offset_x, base_y + (col - 1) * offset_y)

# Move to a specific bank row & column
def bank(col: int, row: int) -> tuple:
    screenWidth, screenHeight = pg.size()
    base_x, base_y = (814 * screenWidth)/2560 , (163 * screenHeight)/1440
    offset_x, offset_y = (72 * screenWidth)/2560 , (55 * screenHeight)/1440
    return (base_x + (col - 1) * offset_x, base_y + (row - 1) * offset_y)

def logout():
    switcher_x, switcher_y = 2344, 1372
    thumbs_up_x, thumbs_up_y = 2287, 1072
    logout_x, logout_y = 2341, 1292

    # Thumbs up and logout
    move(switcher_x, switcher_y)
    select(0)
    move(thumbs_up_x, thumbs_up_y)
    select(0)
    move(logout_x, logout_y)
    select(0)

def login():
    # Adjust pixels for resolution
    login_x, login_y = 1381, 460

    # Get password from .env file in directory
    load_dotenv()
    pwd = os.environ.get('RUNESCAPE_LOGIN')

    # Login
    move(login_x, login_y)
    select(0)
    time.sleep(1)
    for letter in pwd:
        pg.typewrite(letter)
        time.sleep(0.1)
    time.sleep(1)
    pg.press("return")
    move(1275, 530)
    pg.leftClick()

start = dt.now()
move(1280, 720, 0.3)
end = dt.now()
print(end-start)