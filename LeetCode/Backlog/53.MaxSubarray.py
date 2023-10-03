"""
Given an integer array nums, find the
subarray with the largest sum, and return its sum.
"""

def max_subarray(nums: list[int]) -> int:
    # track max sum
    # track cur sum
    max_sum = cur_sum = 0
    # iterate thru nums
    for num in nums:
        if cur_sum <= 0:
            cur_sum = 0
        cur_sum += num
        max_sum = max(max_sum, cur_sum)
        # if prefix sum <= 0:
            # set cur_sum to 0, essentially starting from this idx
        # add cur num to cur sum
        # set max sum to max of max sum/cur sum
    # return max sum
    return max_sum
    pass


print(max_subarray([-2,1,-3,4,-1,2,1,-5,4]) == 6)
print(max_subarray([1]) == 1)
print(max_subarray([5,4,-1,7,8]) == 23)
