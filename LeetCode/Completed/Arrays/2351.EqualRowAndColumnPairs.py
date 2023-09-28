"""
Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) such that row ri and column cj are equal.

A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).
"""
from collections import defaultdict

def equalPairs(grid: list[list[int]]) -> int:
    num_pairs = 0
    col_starts = defaultdict(list)

    for i in range(len(grid[0])):
        col_start = grid[0][i]
        col_starts[col_start].append(i)

    for row in grid:
        idx = 0
        num_matches = 0
        possible_cols = col_starts[row[0]]

        for col in possible_cols:

            while idx < len(row):
                if row[idx] != grid[idx][col]:
                    break
                else:
                    idx += 1
                    num_matches += 1

            if num_matches == len(row):
                num_pairs += 1

            num_matches = 0
            idx = 0

    return num_pairs

print(equalPairs([[3,2,1],[1,7,6],[2,7,7]])) # 1
print(equalPairs([[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]])) # 3
