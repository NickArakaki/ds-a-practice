"""
Given an integer array nums, move all the even
integers at the beginning of the array followed by all the odd integers.

Return any array that satisfies this condition.
"""

def sort_array_by_parity(nums: list[int]) -> list[int]:
    # two pointers init to first el of list
    # move l and r pointers to first odd num
    # move right pointer while inbounds and num ar r is odd
        # if num at r is even swap nums
        # increment pointers
    # return nums
    pass


print(sort_array_by_parity([3,1,2,4]) == [2,4,3,1])
print(sort_array_by_parity([0]) == [0])
