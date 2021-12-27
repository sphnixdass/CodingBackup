
import pyautogui
import random
import time

for i in range(5000):
    pyautogui.moveTo(random.randint(0,200), random.randint(0,200)) 
    time.sleep(random.randint(60,80))

