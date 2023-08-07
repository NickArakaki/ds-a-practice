"""
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.
"""

def search_matrix(matrix: list[list[int]], target: int) -> bool:
    pass


print(search_matrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3) == True)
print(search_matrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13) == False)
