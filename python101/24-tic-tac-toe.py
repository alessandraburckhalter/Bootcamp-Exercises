size = 3
board = []
for y in range(size):
    board.append([])
    for x in range(size):
        board[y].append("[%d][%d]" % (y, x))
      
for row in board:
    for column in row:
        print("%s " % column, end="")
    print("\n")

print("\n\nPlayer X is moving.\n\n")
board[0][2] = "X"

for row in board:
    for column in row:
        print("%s " % column, end="")
    print("\n")

