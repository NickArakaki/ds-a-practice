"""
Given an integer array nums, find the
subarray with the largest sum, and return its sum.
"""

def max_subarray(nums: list[int]) -> int:
    max_sum = cur_sum = 0
    for num in nums:
        if cur_sum < 0:
            cur_sum = 0
        cur_sum += num
        max_sum = max(max_sum, cur_sum)
    return max_sum


print(max_subarray([-2,1,-3,4,-1,2,1,-5,4]) == 6)
print(max_subarray([1]) == 1)
print(max_subarray([5,4,-1,7,8]) == 23)
