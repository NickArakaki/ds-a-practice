"""
Given an m x m matrix grid, which is sorted in non-increase
order both row-wise and column-wise, return the number of negative
numbers in the grid
"""

def countNegatives(grid: list[list[int]]) -> int:
    count = 0

    for r_idx in range(len(grid)):
        for c_idx in range(len(grid[0])):
            curr_value = grid[r_idx][c_idx]
            if curr_value < 0: count += 1

    return count

print(countNegatives([[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]])) # 8
print(countNegatives([[3,2],[1,0]])) # 0
