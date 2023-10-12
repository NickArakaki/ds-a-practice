"""
Given an n x n binary matrix grid, return the length of the
shortest clear path in the matrix. If there is no clear path, return -1.

A clear path in a binary matrix is a path from the top-left cell
(i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

All the visited cells of the path are 0.
All the adjacent cells of the path are 8-directionally connected
(i.e., they are different and they share an edge or a corner).

The length of a clear path is the number of visited cells of this path.
"""

from collections import deque

# def shortest_path_binary_matrix(grid: list[list[int]]) -> int:
#     ROW, COL = len(grid), len(grid[0])

#     if grid[0][0] == 1 or grid[ROW - 1][COL -1] == 1:
#         return -1

#     # queue for bft
#     queue = deque()
#     queue.append([0, 0, 1]) # row, col, num_steps

#     # set for visited nodes
#     visited = set()
#     visited.add((0, 0))

#     # make sure node is inbounds
#     def _inbounds(row, col):
#         row_inbound = 0 <= row and row < ROW
#         col_inbound = 0 <= col and col < COL
#         return row_inbound and col_inbound

#     directions = ((0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1))
#     # create a queue and add first element in matrix
#     while queue:
#     # iterate through queue
#         row, col, num_steps = queue.popleft()
#         # if at end return the length of path traveled
#         if row == ROW - 1 and col == COL - 1:
#             return num_steps
#         # add neighbors if valid
#         for direction in directions:
#             new_row = row + direction[0]
#             new_col = col + direction[1]
#             if _inbounds(new_row, new_col) and (new_row, new_col) not in visited and grid[new_row][new_col] == 0:
#                 queue.append((new_row, new_col, num_steps + 1))
#                 visited.add((new_row, new_col))
#     # if we get to end of queue without making it to the end of the matrix return -1
#     return -1

from heapq import heappop, heappush, heapify
from math import sqrt
# A* method
def shortest_path_binary_matrix(grid: list[list[int]]) -> int:
    # if start or end is a 1 return -1, there needs to be a clear path
    end_r, end_c = len(grid) - 1, len(grid[0]) - 1
    if grid[0][0] == 1 or grid[end_r][end_c] == 1:
        return - 1

    priority_queue = []
    heapify(priority_queue)
    heappush(priority_queue, (sqrt((end_r**2) + (end_c**2)), 1, 0, 0))
    visited = set()
    visited.add((0,0))

    neighbors = ((0,1),(1,0),(0,-1),(-1,0),(1,1),(-1,1),(1,-1),(-1,-1))

    def _is_inbound(r,c):
        r_inbound = 0 <= r < len(grid)
        c_inbound = 0 <= c < len(grid[0])
        return r_inbound and c_inbound

    while priority_queue:
        _, cur_len, r, c = heappop(priority_queue)
        if (r, c) == (end_r, end_c):
            return cur_len

        for neighbor_r, neighbor_c in neighbors:
            new_row = r + neighbor_r
            new_col = c + neighbor_c

            if _is_inbound(new_row, new_col) and grid[new_row][new_col] == 0 and (new_row, new_col) not in visited:
                end_dist = sqrt((end_r - new_row)**2 + (end_c - new_col)**2)
                heappush(priority_queue, (end_dist, cur_len + 1, new_row, new_col))
                visited.add((new_row, new_col))
    return -1

print(shortest_path_binary_matrix([[0,1],[1,0]]) == 2) # 2
print(shortest_path_binary_matrix([[0,0,0],[1,1,0],[1,1,0]]) == 4) # 4
print(shortest_path_binary_matrix([[1,0,0],[1,1,0],[1,1,0]]) == -1) # -1
