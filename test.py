import random
import time

import pyautogui as pg

animal = ["donky", "dog", "monkey"]

time.sleep(3)

for i in range(500):
    rand_animal = random.choice(animal)
    pg.write("you are " + rand_animal)
    pg.press("enter")
