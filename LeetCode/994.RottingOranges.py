"""
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.
"""

def oranges_rotting(grid: list[list[int]]) -> int:
    pass


print(oranges_rotting([[2,1,1],[1,1,0],[0,1,1]]) == 4)
print(oranges_rotting([[2,1,1],[0,1,1],[1,0,1]]) == -1)
print(oranges_rotting([[0,2]]) == 0)
