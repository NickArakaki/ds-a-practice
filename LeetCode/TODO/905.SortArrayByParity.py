"""
Given an integer array nums, move all the even
integers at the beginning of the array followed by all the odd integers.

Return any array that satisfies this condition.
"""

def sort_array_by_parity(nums: list[int]) -> list[int]:
    # two pointers init to first el of list
    l = 0
    # move left pointer to find first odd number
    while l < len(nums) and nums[l] % 2 == 0:
        l += 1

    for r in range(l + 1, len(nums)):
        if nums[r] % 2 == 0:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
    return nums


print(sort_array_by_parity([3,1,2,4]) == [2,4,3,1])
print(sort_array_by_parity([3,4,1,2,3,4,6]) == [4,2,4,6,3,1,3])
print(sort_array_by_parity([0]) == [0])
