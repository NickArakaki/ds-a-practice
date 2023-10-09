"""
    Given an array of ints nums sorted in non-decreasing order,
    find the starting and ending position of a given target val

    If target is not found in the arr, return [-1, -1]

    You must write the algo with O(logn) runtime complexity
"""


def search_range(nums: list[int], target: int) -> list[int]:
    start = end = -1

    # two bin search
    l, r = 0, len(nums) - 1
    while l <= r:
        # calculate mid
        mid = l + (r - l) // 2
        if (mid == 0 or nums[mid - 1] < target) and nums[mid] == target:
            start = mid
            break
        elif nums[mid] < target:
            l = mid + 1
        else:
            r = mid - 1

    # second for end
    if start == -1:
        return [start, end]

    l, r = start, len(nums) - 1
    while l <= r:
        mid = l + (r - l) // 2
        if (mid == len(nums) - 1 or nums[mid + 1] > target) and nums[mid] == target:
            end = mid
            break
        elif nums[mid] > target:
            r = mid - 1
        else:
            l = mid + 1

    return [start, end]



print(search_range([5,7,7,8,8,10], 8) == [3,4])
print(search_range([5,7,7,8,8,10], 6) == [-1,-1])
print(search_range([5], 5) == [0,0])
print(search_range([], 0) == [-1, -1])
