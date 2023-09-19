"""
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only constant extra space.
"""

def find_duplicate(nums: list[int]) -> int:
    for i, cur_num in enumerate(nums):
        for next_num in nums[i + 1:]:
            if cur_num == next_num:
                return cur_num
    return -1

print(find_duplicate([1,3,4,2,2]) == 2)
print(find_duplicate([3,1,3,4,2]) == 3)
