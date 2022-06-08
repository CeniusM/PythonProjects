import TicTacToe as TTT
import time
import math

start_time = time.time()
# start

# inside vsc
# 14m
# 850sec
# 858236ms

reps = 1000000 #1m
rep = 0

moves = [0, 1, 2, 3, 4, 5, 6, 7, 8];

while rep < reps:
    ttt = TTT.TicTacToe(rep)

    i = 0
    while i < 9:
        ttt.MakeMove(i)
        i += 1
    
    i = 0
	# rotates the moves
    move0 = moves[0];
    while i < 8:
        moves[i] = moves[i + 1];
        i += 1
    moves[8] = move0;

    rep += 1

# end
end_time = time.time()

time_spent = end_time - start_time

print(int(time_spent * 1000), "ms")

input()