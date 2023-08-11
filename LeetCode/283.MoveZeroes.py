"""
Given an integer array nums, move all 0's to the end
of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.
"""

def move_zeroes(nums: list[int]) -> list[int]:
    r = 0
    for l in range(len(nums)):
        while r < len(nums) and nums[r] == 0:
            r += 1

        if nums[l] == 0 and l < r and r < len(nums):
            nums[l], nums[r] = nums[r], nums[l]
            r += 1
    print(nums)
    return nums

print(move_zeroes([0,1,0,3,12]) == [1,3,12,0,0])
print(move_zeroes([1,3,0,12,0]) == [1,3,12,0,0])
print(move_zeroes([0]) == [0])
print(move_zeroes([1, 0]) == [1, 0])
