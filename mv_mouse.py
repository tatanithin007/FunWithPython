import time
from itertools import cycle
from random import randint
import pyautogui

#infinate for loop 
for t in cycle(range(0, 4)):

    time.sleep(10)
    # makes program execution pause for 10 sec
    pyautogui.moveTo(randint(100,1000), randint(100,1000), duration=1)
    #above line will move mouse pointer into random points over the screen
