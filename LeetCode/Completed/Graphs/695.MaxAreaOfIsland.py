"""
You are given an m x n binary matrix grid. An island is a
group of 1's (representing land) connected 4-directionally
(horizontal or vertical.) You may assume all four edges of the
grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.
"""

def max_area_of_island(grid: list[list[int]]) -> int:

    def _dfs(row, col):
        if not _in_bounds(row, col):
            return 0

        pos = (row, col)
        if pos in visited:
            return 0

        if grid[row][col] == 0:
            return 0

        visited.add(pos)
        curr_island = 1

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for direction in directions:
            new_row = row + direction[0]
            new_col = col + direction[1]
            curr_island += _dfs(new_row, new_col)

        return curr_island


    def _in_bounds(row, col):
        row_inbound = row >= 0 and row < len(grid)
        col_inbound = col >= 0 and col < len(grid[0])
        return row_inbound and col_inbound


    max_island = 0
    visited = set()

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            curr_area = _dfs(row, col)
            max_island = max(max_island, curr_area)

    return max_island


print(max_area_of_island([[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]])) # 6
print(max_area_of_island([[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]) == 6) # 6
print(max_area_of_island([[0,0,0,0,0,0,0,0]])) # 0
print(max_area_of_island([[0,0,0,0,0,0,0,0]]) == 0) # 0
