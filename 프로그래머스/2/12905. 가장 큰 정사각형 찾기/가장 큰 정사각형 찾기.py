def solution(board):
    X, Y = len(board), len(board[0])
    max_length = 0
    for x in range(1, X):
        for y in range(1, Y):
            if board[x][y] == 1:
                board[x][y] = min(board[x-1][y-1], board[x][y-1], board[x-1][y]) + 1
    for i in range(X):
        max_length = max(max_length, max(board[i]))
    return max_length * max_length