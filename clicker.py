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
    
    # Generate a random point between co-ords
    mid_x = sorted(np.random.uniform(min(start_x, end_x), max(start_x, end_x), size = 2))
    mid_y = sorted(np.random.uniform(min(start_y, end_y), max(start_y, end_y), size = 2))

    # Generate Bezier curve
    nodes = np.asarray([
        [start_x] + mid_x + [end_x],
        [start_y] + mid_y + [end_y]
    ])

    curve = bz.Curve(nodes, degree = 3, copy = False)
    return curve

# Normalize co-ordinates for different screen sizes
def normalize(x: int, y: int) -> tuple:
    screen_width, screen_height = pg.size()
    x = (x * screen_width) // 2560
    y = (y * screen_height) // 1440
    return (x, y)


# Move mouse to location
def move(x: int, y: int, speed: float = 1, points: float = 15, spread: int = 2) -> None:
    
    # Normally distribute start & end coords
    curr_x, curr_y = pg.position()
    rand_x = round(np.random.normal(x, spread)) 
    rand_y = round(np.random.normal(y, spread))

    # Normally distribute speed
    rand_speed = np.random.uniform(speed/2, speed) * (1/points)

    # Easing functions for random choice of mouse movement
    tweens = [pg.easeOutBack, pg.easeOutQuad, pg.easeOutCubic, pg.easeOutExpo, pg.easeInQuad, pg.easeInCubic, pg.easeInExpo]
    
    # Generate and split bezier curve
    curve = make_curve((curr_x, curr_y), (rand_x, rand_y))
    curve_points = sorted(np.random.uniform(0.01, 0.99, points)) + [1]
    curve_coords = map(np.around, map(curve.evaluate, curve_points))

    # Move along the curve
    for pos in curve_coords: 
        next_x, next_y = pos
        pg.moveTo(next_x, next_y, rand_speed, tween = (np.random.choice(tweens) if (next_x == rand_x and next_y == rand_y) else pg.linear))


# Select Option 
def select(option: int) -> None:

    # Screen resolution for scaling
    x_offset, y_offset = normalize(10, 38)
    res_y = pg.size()[1]
    y_option_offset = round((23 * res_y)//1440)

    # M1 click
    if option == 0:
        pg.leftClick()
        return

    # M2 Option Select
    pg.rightClick()
    curr_x, curr_y = pg.position()
    rand_x = curr_x + x_offset
    rand_y = curr_y + y_offset + (y_option_offset * (option - 1)) 
    move(rand_x, rand_y, speed = 0.6, spread = 1)
    pg.leftClick()


# Moves to a specific inventory row & column
def inventory(col: int, row: int) -> tuple:
    base_x, base_y = normalize(2246, 986)
    offset_x, offset_y = normalize(65, 55)
    return (base_x + (col - 1) * offset_x, base_y + (row - 1) * offset_y)

# Move to a specific bank row & column
def bank(col: int, row: int) -> tuple:
    base_x, base_y = normalize(814, 163)
    offset_x, offset_y = normalize(72, 55)
    return (base_x + (col - 1) * offset_x, base_y + (row - 1) * offset_y)


def logout():
    switcher_x, switcher_y = normalize(2344, 1372)
    logout_x, logout_y = normalize(2341, 1292)

    # Thumbs up and logout
    move(switcher_x, switcher_y)
    pg.leftClick()
    move(logout_x, logout_y)
    pg.leftClick()


def login():
    # Co ordinates for login
    login_x, login_y = normalize(1381, 460)
    click_x, click_y = normalize(1275, 530)

    # Get password from .env file in directory
    load_dotenv()
    pwd = os.environ.get('RUNESCAPE_LOGIN')

    # Login
    move(login_x, login_y)
    pg.leftClick()
    time.sleep(np.random.uniform(0.5, 1))
    for letter in pwd:
        pg.typewrite(letter)
        time.sleep(np.random.uniform(0.1, 0.3))
    time.sleep(np.random.uniform(0.5, 1))
    pg.press("return")
    time.sleep(np.random.uniform(4, 7))
    move(click_x, click_y, spread = 10)
    pg.leftClick()