"""
    Given an array of ints nums sorted in non-decreasing order,
    find the starting and ending position of a given target val

    If target is not found in the arr, return [-1, -1]

    You must write the algo with O(logn) runtime complexity
"""


def search_range(nums: list[int], target: int) -> list[int]:
    # start = end = -1
    # two bin search
    # init l and r pointers
    # first for start
    # iterate while l <= r
        # calculate mid
        # if mid == 0 or nums[mid - 1] < target and nums[mid] == target, found start
        # elif nums[mid] > target: search right
        # else search left

    # second for end
    # set l pointer to start if start >= -1 else 0, r pointer to end of nums
    # while l <= r:
        # calculate mid
        # if mid == len(nums) - 1 or nums[mid + 1] > target and nums[mid] == target, found end
        # elif nums[mid] < target: search left
        # else: search right

    # return [start, end]



print(search_range([5,7,7,8,8,10], 8) == [3,4])
print(search_range([5,7,7,8,8,10], 6) == [-1,-1])
print(search_range([], 0) == [-1, -1])
