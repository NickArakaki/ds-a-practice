"""
Given an m x n matrix, if an
element is 0, set its entire row and
column to 0's

You must do it in place

Constraints:
    m == matrix.length

    n == matrix[0].length

    1 <= m, n <= 200

    -231 <= matrix[i][j] <= 231 - 1
"""

def setZeroes(matrix):
    rows = set()
    cols = set()

    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == 0:
                rows.add(row)
                cols.add(col)

    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if row in rows or col in cols:
                matrix[row][col] = 0

    return matrix

print(setZeroes([[1,1,1],
                 [1,0,1],
                 [1,1,1]])) # [[1,0,1],
                            #  [0,0,0],
                            #  [1,0,1]]
print(setZeroes([[0,1,2,0],
                 [3,4,5,2],
                 [1,3,1,5]])) # [[0,0,0,0],
                              #  [0,4,5,0],
                              #  [0,3,1,0]]
