def Solve(board, column, n, n_queen, counter):
    if n_queen >= n:
        print(board)
        print()
        return
    for i in range(n):
        if checkSolve(board, i, column, n):
            board[i][column] = 1
            Solve(board, column+1, n, n_queen + 1, counter + 1)
        board[i][column] = 0
def checkSolve(board, row, column, n):
    if row == n:
        return False
    if column == n:
        return False
    #Upper Check
    for i in range(0, row+1):
        if board[i][column] == 1:
            return False
    #Lower Check
    for i in range(row+1, n):
        if board[i][column] == 1:
            return False
    #Left Check
    for j in range(0, column+1):
        if board[row][j] == 1:
            return False
    #right Check
    for j in range(column+1, n):
        if board[row][j] == 1:
            return False
    #upper Diagonal
    i = row - 1 
    j = column - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
             return False
        i -= 1
        j -= 1
    #Lower Diagonal
    i = row + 1
    j = column - 1
    while i < n and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1
    return True

n=5
board = [[0,0,0,0,0],
         [0,0,0,0,0],
         [0,0,0,0,0],
         [0,0,0,0,0],
         [0,0,0,0,0]]
print(board)
print(Solve(board, 0, n, 0, 0))