"""
Given an array of positive integers nums and a positive integer target, return the minimal length of a
subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

Constraints:
    1 <= target <= 109
    1 <= nums.length <= 105
    1 <= nums[i] <= 104
"""

def minSubArrayLen(target, nums):
    l, r = 0, 0

    min_length = float("inf")

    curr_sum = 0

    while r < len(nums):
        if curr_sum < target:
            curr_sum += nums[r]
            r += 1

        while curr_sum >= target:
            min_length = min(min_length, (r - l))
            curr_sum -= nums[l]
            l += 1

    return min_length if min_length != float("inf") else 0

print(minSubArrayLen(7, [2,3,1,2,4,3])) # 2
print(minSubArrayLen(4, [1,4,4])) # 1
print(minSubArrayLen(11, [1,1,1,1,1,1,1,1]))# 0
