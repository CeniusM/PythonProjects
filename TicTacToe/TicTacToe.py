import array

class TicTacToe:
    def __init__(self, gameID):
        self.gameId = gameID
        self.board = array.array('i',(0 for i in range(0,10)))
        self.player = 0
        self.turn = 0
        self.winner = 0
        self.isGameOver = False
    
    def MakeMove(self, move):
        if self.board[move] != 0:
            return False
        if self.isGameOver:
            return False

        self.board[move] = self.player
        self.turn += 1

        if self.turn == 9:
            self.winner = self.player
            self.isGameOver = True
            return True

        if self.GameOverCheck():
            self.winner = self.player
            self.isGameOver = True
            return True
        
        if self.player == 1:
            self.player = 2
        else:
            self.player = 1

    def GameOverCheck(self):
        j = 0
        for i in range(0,3):
            j = i * 3
            if self.board[i] != 0:
                if self.board[i] == self.board[i + 3]:
                    if self.board[i + 3] == self.board[i + 6]:
                        return True
            if self.board[j] != 0:
                if self.board[j] == self.board[j + 1]:
                    if self.board[j + 1] == self.board[j + 2]:
                        return True
        
        if self.board[0] != 0:
            if self.board[0] == self.board[4]:
                if self.board[4] == self.board[8]:
                    return True

        if self.board[2] != 0:
            if self.board[2] == self.board[4]:
                if self.board[4] == self.board[6]:
                    return True

        return False