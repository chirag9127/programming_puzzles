"""
Given a board with m by n cells, each cell has an initial state live (1) or
dead (0). Write a function to compute the next state (after one update) of the
board given its current state.
"""


def game_of_life(board):
    row_len = len(board)
    col_len = len(board[0])
    for i in range(row_len):
        for j in range(col_len):
            num_live_neighbors = count_neighbors(i, j, row_len, col_len, board)
            if board[i][j] == 1:
                if num_live_neighbors < 2 or num_live_neighbors > 3:
                    board[i][j] = -1
            else:
                if num_live_neighbors == 3:
                    board[i][j] = 2
    for i in range(row_len):
        for j in range(col_len):
            if board[i][j] == -1:
                board[i][j] = 0
            elif board[i][j] == 2:
                board[i][j] = 1


def count_neighbors(i, j, row_len, col_len, board):
    count = 0
    for x, y in (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1), \
            (i - 1, j - 1), (i - 1, j + 1), (i + 1, j - 1), (i + 1, j + 1):
        if 0 <= x < row_len and 0 <= y < col_len:
            if board[x][y] in [1, -1]:
                count += 1
    return count
