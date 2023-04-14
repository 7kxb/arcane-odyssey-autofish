import pyautogui
from pynput.keyboard import Key,Controller
import keyboard
import time
import os
pyautogui.PAUSE = 0.1
c = True
n = 0
t = 0
pyautogui.moveTo(800,800)
pyautogui.click()
for i in range(9):
  Controller().press('i')
  time.sleep(pyautogui.PAUSE)
  Controller().release('i')
for i in range(2):
  Controller().press('o')
  time.sleep(pyautogui.PAUSE)
  Controller().release('o')
while not keyboard.is_pressed('q'):
  s = pyautogui.locateCenterOnScreen('F.png',region=(0,0,1920,1080),grayscale=True,confidence=0.80)
  if s is not None:
    pyautogui.moveTo(s)
    for i in range(60):
      pyautogui.click()
    c = True
  elif s is None and (c or t > 240):
    Controller().press('w')
    time.sleep(pyautogui.PAUSE*0.6)
    Controller().release('w')
    pyautogui.click()
    c = False
    n += 1
    t = 0
  else:
    t += 1
    os.system('cls' if os.name == 'nt' else 'clear')
    print(n,t)