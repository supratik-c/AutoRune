import keyboard as kb
import time
import pyautogui as pg

# Record co-ordinates of mouse position
def pos():
    while True:
        if kb.is_pressed("q"):
            (x, y) = pg.position()
            print(x, ",", y, sep = "")
            time.sleep(1.5)
        elif kb.is_pressed("e"):
            break

if __name__ == "__main__":
    pos()