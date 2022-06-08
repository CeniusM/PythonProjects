import TicTacToe as TTT

def PrintBoard(ttt):
    print(ttt.board[0], ttt.board[1], ttt.board[2])
    print(ttt.board[3], ttt.board[4], ttt.board[5])
    print(ttt.board[6], ttt.board[7], ttt.board[8])

game = TTT.TicTacToe(1);
gameRunning = True

while gameRunning:
    myInput = input()

    if myInput == 'stop':
        gameRunning = False
        break

    if myInput.isnumeric() == False:
        continue
    
    if int(myInput) > 8:
        if int(myInput) < 0:
            continue
    
    game.MakeMove(int(myInput))

    if game.isGameOver:
        gameRunning = False

    PrintBoard(game)

print("done")

input()