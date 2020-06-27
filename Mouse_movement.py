# program to move the mouse
import pyautogui as p 

print("you are about to see magic")
for i in range(10):
    p.moveTo(100, 100, duration=0.5)
    p.moveTo(200, 100, duration=0.5)
    p.moveTo(200, 200, duration=0.5)
    p.moveTo(100, 200, duration=0.5)
print("finished")
    