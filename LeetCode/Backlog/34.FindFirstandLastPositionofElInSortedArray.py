"""
    Given an array of ints nums sorted in non-decreasing order,
    find the starting and ending position of a given target val

    If target is not found in the arr, return [-1, -1]

    You must write the algo with O(logn) runtime complexity
"""


def search_range(nums: list[int], target: int) -> list[int]:
    target_range = [-1, -1]

    return target_range



print(search_range([5,7,7,8,8,10], 8) == [3,4])
print(search_range([5,7,7,8,8,10], 6) == [-1,-1])
print(search_range([], 0) == [-1, -1])
