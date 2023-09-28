"""
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.
"""

def search_matrix(matrix: list[list[int]], target: int) -> bool:
    l, r = 0, len(matrix) - 1

    while l <= r:
        mid = l + (r - l) // 2
        row = matrix[mid]

        if target < row[0]:
            r = mid - 1
        elif target > row[-1]:
            l = mid + 1
        if row[0] <= target and target <= row[-1]:
            return bin_search(row, target)
    return False


def bin_search(nums: list[int], target: int) -> bool:
    l, r = 0 , len(nums) - 1
    while l <= r:
        mid = l + (r - l) // 2
        if target < nums[mid]:
            r = mid - 1
        elif target > nums[mid]:
            l = mid + 1
        else:
            return True

    return False


print(search_matrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3) == True)
print(search_matrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13) == False)
print(search_matrix([[1]], 1) == True)
