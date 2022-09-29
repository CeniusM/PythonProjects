import pyautogui
from random import randint

def Click(x,y) -> None:
    pyautogui.moveTo(x,y)
    #win32api.SetCursorPos((x,y))
    # win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,20,200,0,0)
    # win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,20,200,0,0)
    
def Rand(min: int = 0, max: int = 1) -> int:
    return randint(min, max)
def main():
    #SAP poses
    poses = [(530,444) ,(666,444) ,(814,444) ,(960,444) ,(1111,444),(530,700),(666,700),(814,700),(960,700),(1111,700),(1255,700),(1400,700),(328,1000)]

    # active pets 
    # shop pets/food
    # roll

    # end turn
    endTurnPos = (1500, 1000)

    # while(True):
    #     print(win32api.GetCursorPos())
    for _ in range(10):
        x,y = poses[Rand(0, len(poses)-1)]
        Click(x,y)
    # Click(endTurnPos[0], endTurnPos[1])
    Click(0,0)
    Click(poses[0][0], poses[0][1])

    #1535, 863 is apparently the real range on the screen
if __name__ == "__main__":
    main()