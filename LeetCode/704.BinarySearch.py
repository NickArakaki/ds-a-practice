"""
Given an array of integers nums which is sorted in ascending order,
and an integer target, write a function to search target in nums.
If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

Constraints:

1 <= nums.length <= 104

-104 < nums[i], target < 104

All the integers in nums are unique.

nums is sorted in ascending order.
"""


def search(nums: list[int], target: int) -> int:
    l, r = 0, len(nums) - 1

    while l <= r:
        mid = r + l // 2

        if nums[mid] == target:  # found target
            return mid
        elif target < nums[mid]:  # search left
            r = mid - 1
        else:  # search right
            l = mid + 1

    return -1  # target not found


print(search([-1, 0, 3, 5, 9, 12], 9))  # 4
print(search([-1, 0, 3, 5, 9, 12], 2))  # -1
