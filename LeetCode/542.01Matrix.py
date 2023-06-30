"""
Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.
"""
from collections import deque

def update_matrix(mat: list[list[int]]) -> list[list[int]]:
    ROW, COL = len(mat), len(mat[0])

    directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
    def _inbound(row, col):
        row_inbound = 0 <= row and row < ROW
        col_inbound = 0 <= col and col < COL
        return row_inbound and col_inbound

    # iterate through mat
    for r in range(ROW):
        for c in range(COL):
            if mat[r][c] == 1:
                queue = deque()
                visited = set()
                queue.append((r, c, 0)) # row, col, distance
                visited.add((r, c))

                # do bft to find min distance to nearest 0
                while queue:
                    curr_row, curr_col, distance = queue.popleft()

                    if mat[curr_row][curr_col] == 0:
                        mat[r][c] = distance
                        break

                    for direction in directions:
                        new_row = curr_row + direction[0]
                        new_col = curr_col + direction[1]

                        if _inbound(new_row, new_col) and (new_row, new_col) not in visited:
                            queue.append((new_row, new_col, distance + 1))
                            visited.add((new_row, new_col))


    return mat


print(update_matrix([[0,0,0],[0,1,0],[0,0,0]]) == [[0,0,0],[0,1,0],[0,0,0]])
print(update_matrix([[0,0,0],[0,1,0],[1,1,1]]) == [[0,0,0],[0,1,0],[1,2,1]])
