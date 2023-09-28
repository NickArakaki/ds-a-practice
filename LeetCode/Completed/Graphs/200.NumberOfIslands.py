"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four
edges of the grid are all surrounded by water.
"""

def num_islands(grid: list[list[str]]) -> int:

    def _dfs(row, col):
        if not _in_bounds(row, col):
            return False

        pos = (row, col)
        if pos in visited:
            return False

        if grid[row][col] == "0":
            return False

        visited.add(pos)
        directions = ((1,0), (0,1), (-1, 0), (0, -1))
        for direction in directions:
            new_row = row + direction[0]
            new_col = col + direction[1]
            _dfs(new_row, new_col)

        return True


    def _in_bounds(row, col):
        row_inbound = 0 <= row and row < len(grid)
        col_inbound = 0 <= col and col < len(grid[0])
        return row_inbound and col_inbound

    count = 0
    visited = set()

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if _dfs(row, col):
                count += 1

    return count

print(num_islands([
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
])) # 1

print(num_islands([
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
])) # 3
