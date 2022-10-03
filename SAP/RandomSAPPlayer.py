from time import sleep
import pyautogui
from random import randint


def Click(x: int, y: int) -> None:
    pyautogui.moveTo(x, y)
    pyautogui.click()


def Rand(min: int = 0, max: int = 1) -> int:
    return randint(min, max)


def main():
    # PrintCoords()
    sleep(2)
    # SAP poses
    poses = [(530, 444), (666, 444), (814, 444), (960, 444), (1111, 444), (530, 700), (1300, 1000),
             (666, 700), (814, 700), (960, 700), (1111, 700), (1255, 700), (1400, 700), (328, 1000)]

    # active pets
    # shop pets/food
    # roll

    # end turn
    endTurnPos = (1500, 1000)

    # while(True):
    #     print(win32api.GetCursorPos())
    for _ in range(100):
        x, y = poses[Rand(0, len(poses)-1)]
        Click(x, y)
    Click(endTurnPos[0], endTurnPos[1])


def PrintCoords():
    print('Press Ctrl-C to quit.')
    try:
        while True:
            x, y = pyautogui.position()
            positionStr = f"X: {str(x).rjust(4)} Y: {str(y).rjust(4)}"
            print(positionStr, end='')
            print('\b' * len(positionStr), end='', flush=True)
    except KeyboardInterrupt:
        print('\n')


    # 1535, 863 is apparently the real range on the screen
if __name__ == "__main__":
    # PrintCoords()
    main()
