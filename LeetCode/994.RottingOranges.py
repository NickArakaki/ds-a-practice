"""
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.
"""

from collections import deque

def oranges_rotting(grid: list[list[int]]) -> int:
    ROW, COL = len(grid), len(grid[0])
    # initialize a queue for a bft
    queue = deque()
    # initialize a set to keep track of visited node
    visited = set()
    # add every position that == 2 to queue and set
    for r in range(ROW):
        for c in range(COL):
            if grid[r][c] == 2:
                queue.append((r, c, 0)) # row, col, curr_min
                visited.add((r, c))

    # initialize a max_time var to track max num minutes for rotten oranges to visit all possible oranges
    max_time = 0

    directions = ((1, 0), (0, 1), (-1, 0), (0, -1))

    def _inbound(row, col):
        row_inbound = 0 <= row and row < ROW
        col_inbound = 0 <= col and col < COL
        return row_inbound and col_inbound

    # run bft on the initialized queue
    while queue:
        # get valid neighbors
        curr_r, curr_c, curr_time = queue.popleft()
        max_time = max(max_time, curr_time)
        # if neighbor not in visited
        for direction in directions:
            new_row = curr_r + direction[0]
            new_col = curr_c + direction[1]
            if _inbound(new_row, new_col) and (new_row, new_col) not in visited and grid[new_row][new_col] == 1:
                visited.add((new_row, new_col))
                queue.append((new_row, new_col, curr_time + 1))

    for r in range(ROW):
        for c in range(COL):
            if (r, c) not in visited and grid[r][c] == 1:
                return -1

    return max_time

print(oranges_rotting([[2,1,1],[1,1,0],[0,1,1]]) == 4)
print(oranges_rotting([[2,1,1],[0,1,1],[1,0,1]]) == -1)
print(oranges_rotting([[0,2]]) == 0)
