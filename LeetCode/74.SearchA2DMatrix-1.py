"""
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

Constraints

m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-104 <= matrix[i][j], target <= 104
"""

def searchMatrix(matrix:list[list[int]], target:int) -> bool:
    l, r = 0, len(matrix) - 1

    while l <= r:
        mid = l + (r - l) // 2

        row = matrix[mid]

        if row[0] > target: # discard values to the right
            r = mid - 1
        elif row[-1] < target: # discard values to the left
            l = mid + 1
        if row[0] <= target and row[-1] >= target:
            return binarySearch(row, target)

    return False


def binarySearch(nums:list[int], target:int) -> bool:
    """
    input: integer list, target integer
    output: boolean

    using binary search to determine if target is in int list
    """

    l, r = 0, len(nums) - 1

    while l <= r:
        mid = l + (r - l) // 2
        if nums[mid] < target:
            l = mid + 1
        elif nums[mid] > target:
            r = mid - 1
        else:
            return True

    return False


print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3)) # true
print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13)) # false
