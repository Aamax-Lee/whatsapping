import pyautogui
import time

limit = int(input("Enter limit: "))
message = input("Enter message: ")
i = 0

'''delays the execution'''
time.sleep(3)

while i < limit:
   
   pyautogui.typewrite(message)
   pyautogui.press("enter")

   i += 1