import keyboard as kb
import time
import pyautogui as pg

# Record co-ordinates of mouse position
def pos():
    recording = True
    while recording:
        if kb.is_pressed("q"):
            (x, y) = pg.position()
            print("Position: ", x, ", ", y)
            time.sleep(1.5)
        elif kb.is_pressed("e"):
            break