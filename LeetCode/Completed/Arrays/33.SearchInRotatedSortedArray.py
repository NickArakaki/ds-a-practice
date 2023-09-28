"""
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.
"""

def search(nums: list[int], target: int) -> int:
    l, r = 0, len(nums) - 1

    while l <= r:
        mid = l + (r - l) // 2
        num = nums[mid]

        if target == num:
            return mid

        if nums[l] <= nums[mid]:
            if target > nums[mid] or target < nums[l]: # search right
                l = mid + 1
            else:
                r = mid - 1
        else:
            if target < nums[mid] or target > nums[r]: # search left
                r = mid - 1
            else:
                l = mid + 1

    return -1


print(search([4,5,6,7,0,1,2], 0) == 4)
print(search([4,5,6,7,0,1,2], 3) == -1)
print(search([1,2,3,4,5,6,7], 1) == 0)
print(search([1], 0) == -1)
print(search([0], 0) == 0)
