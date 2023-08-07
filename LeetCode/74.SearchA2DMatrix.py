"""
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.
"""

def search_matrix(matrix: list[list[int]], target: int) -> bool:
    # bin search through first level of lists
    # bin search within the list that could contain target
        # return true if found
    # return false if not found after bin searches
    l1, r1 = 0, len(matrix) - 1
    while l1 < r1: # outer bin search
        mid1 = (l1 + r1) // 2
        curr_list = matrix[mid1]
        if curr_list[0] <= target and curr_list[-1] >= target:
            # do inner bin search
            l2, r2 = 0, len(curr_list) - 1
            while l2 < r2:
                mid2 = (l2 + r2) // 2
                if curr_list[mid2] == target:
                    return True
                elif target < curr_list[mid2]: # search left
                    r2 = mid2
                else:
                    l2 = mid2 + 1
        elif target < curr_list[-1]: # search left
            r1 = mid1
        else:
            l1 = mid1 + 1
    return False


print(search_matrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3) == True)
print(search_matrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13) == False)
