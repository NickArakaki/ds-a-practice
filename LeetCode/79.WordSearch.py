"""
Given an m x n grid of characters board and a string word,
return true if word exists in the grid.

The word can be constructed from letters of sequentially
adjacent cells, where adjacent cells are horizontally or
vertically neighboring. The same letter cell may not be used more than once.
"""

def exist(board: list[list[str]], word: str) -> bool:
    pass

print(exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED")) # true
print(exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE")) # true
print(exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB")) # false
