from pydoc import cli
import win32api, win32con
from time import sleep as Sleep
from random import randint

def Click(x,y):
    win32api.SetCursorPos((x,y))
    # win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,20,200,0,0)
    # win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,20,200,0,0)
    
def Rand(min: int = 0, max: int = 1):
    return randint(min, max)

#SAP poses
poses = []
# active pets
poses.append({530,444})
poses.append({666,444})
poses.append({814,444})
poses.append({960,444})
poses.append({1111,444})
# shop pets/food
poses.append({530,700})
poses.append({666,700})
poses.append({814,700})
poses.append({960,700})
poses.append({1111,700})
poses.append({1255,700})
poses.append({1400,700})
# roll
poses.append({328,1000})

# end turn
endTurnPos = {1500, 1000}

while(True):
    print(win32api.GetCursorPos())
for _ in range(10):
    x,y = poses[Rand(0, poses.__len__() - 1)]
    Click(x,y)
Click(endTurnPos[0], endTurnPos[1])

Click(poses[0][0], poses[0][1])

#1535, 863 is apparently the real range on the screen