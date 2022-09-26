import win32api, win32con
from time import sleep as Sleep
from random import seed
from random import randint

def Click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,20,200,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,20,200,0,0)
    
# generate some integers
for _ in range(10):
	value = randint(0, 10)
	print(value)