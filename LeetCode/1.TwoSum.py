"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Constraints:
    2 <= nums.length <= 104
    -109 <= nums[i] <= 109
    -109 <= target <= 109
    Only one valid answer exists.
"""

def twoSum(nums, target):
    # init a hash map with the num as the key, with the index value as the value
    target_nums = {}

    # iterate through nums
    for i, num in enumerate(nums):
        # calc diff
        diff = target - num
        # if diff in target_nums, we found the other value
        if diff in target_nums:
            return [target_nums[diff], i]
        # else add to target_nums
        else:
            target_nums[num] = i

    # Don't need anything but the loop because we're assuming there will always be one, and only one solution

print(twoSum([2,7,11,15], 9)) # [0, 1]
print(twoSum([3,2,4], 6)) # [1, 2]
print(twoSum([3,3], 6)) # [0, 1]
