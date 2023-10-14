"""
Given a 4x4 matrix mat, the initial energy is 100. The task is to reach the
last row of the matrix with the max possible energy left.

The mat can be traversed in the following way:
    1. Start with any cell in the first row
    2. In each move, traverse the cell(i, j) of the ith row and jth col to
        any existing cell out of (i + 1, j - 1), (i + 1, j), (i + 1, j + 1)

After stepping on a cell (i, j), energy decreases by mat[i][j] units. Find the max possible
energy left at the end of the traversal

Note: final energy can be negative


"""

def maxEnergy(mat: list[list[int]]) -> int:
    # Write your code here
    dp = mat[-1]
    for i in range(len(mat) - 2, -1, -1):
        row = mat[i]
        cur_cost = []

        for j, val in enumerate(row):
            l = float("inf") if j <= 0 else dp[j - 1]
            r = float("inf") if j >= len(row) - 1 else dp[j + 1]
            c = dp[j]
            cur_cost.append(val + min(l,r,c))

        dp = cur_cost

    return 100 - min(dp)


print(maxEnergy([[10,20,30,40], [60,50,20,80], [10,10,10,10], [60,50,60,50]]) == 0)
