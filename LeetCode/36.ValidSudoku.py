"""
Determine if a 9 x 9 Sudoku board is valid.
Only the filled cells need to be validated
according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the
digits 1-9 without repetition.

Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
"""
from collections import defaultdict

def isValidSudoku(board):
    rows = defaultdict(set)
    cols = defaultdict(set)
    boxes = defaultdict(set)

    for row in range(len(board)):
        for col in range(len(board[0])):
            value = board[row][col]

            if value != ".":
                if row in rows and value in rows[row]:
                    return False
                else:
                    rows[row].add(value)

                if col in cols and value in cols[col]:
                    return False
                else:
                    cols[col].add(value)

                if (row // 3, col // 3) in boxes and value in boxes[(row // 3, col // 3)]:
                    return False
                else:
                    boxes[(row // 3, col // 3)].add(value)

    return True

print(isValidSudoku([["5","3",".",".","7",".",".",".","."]
                    ,["6",".",".","1","9","5",".",".","."]
                    ,[".","9","8",".",".",".",".","6","."]
                    ,["8",".",".",".","6",".",".",".","3"]
                    ,["4",".",".","8",".","3",".",".","1"]
                    ,["7",".",".",".","2",".",".",".","6"]
                    ,[".","6",".",".",".",".","2","8","."]
                    ,[".",".",".","4","1","9",".",".","5"]
                    ,[".",".",".",".","8",".",".","7","9"]])) # true

print(isValidSudoku([["8","3",".",".","7",".",".",".","."]
                    ,["6",".",".","1","9","5",".",".","."]
                    ,[".","9","8",".",".",".",".","6","."]
                    ,["8",".",".",".","6",".",".",".","3"]
                    ,["4",".",".","8",".","3",".",".","1"]
                    ,["7",".",".",".","2",".",".",".","6"]
                    ,[".","6",".",".",".",".","2","8","."]
                    ,[".",".",".","4","1","9",".",".","5"]
                    ,[".",".",".",".","8",".",".","7","9"]])) # false
