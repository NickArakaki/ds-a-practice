"""
Given an m x m matrix grid, which is sorted in non-increase
order both row-wise and column-wise, return the number of negative
numbers in the grid
"""

# def countNegatives(grid: list[list[int]]) -> int:
#     count = 0

#     for r_idx in range(len(grid)):
#         for c_idx in range(len(grid[0])):
#             curr_value = grid[r_idx][c_idx]
#             if curr_value < 0: count += 1

#     return count

def countNegatives(grid: list[list[int]]) -> int:
    count = 0

    for row in grid:
        # BS for each row to find first instance of value < 0
        l, r = 0, len(row) - 1
        first_neg = None
        while l <= r:
            mid = (r + l)  // 2
            if row[mid] < 0: # need to check vals to the left
                first_neg = mid
                r = mid - 1
            else: # need to check vals to right
                l = mid + 1

        if first_neg is not None:
            count += len(row) - first_neg

    return count

print(countNegatives([[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]])) # 8
print(countNegatives([[3,2],[1,0]])) # 0
