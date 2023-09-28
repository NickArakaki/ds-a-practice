"""
Given an integer array nums, move all 0's to the end
of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.
"""

def move_zeroes(nums: list[int]) -> list[int]:
    l = 0

    for r in range(len(nums)):
        if nums[r] != 0:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1

    return nums

print(move_zeroes([0,1,0,3,12]) == [1,3,12,0,0])
print(move_zeroes([1,3,0,12,0]) == [1,3,12,0,0])
print(move_zeroes([0]) == [0])
print(move_zeroes([1, 0]) == [1, 0])
