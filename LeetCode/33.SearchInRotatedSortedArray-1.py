"""
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown
pivot index k (1 <= k < nums.length) such that the resulting array is
[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).
For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target,
return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

Constraints

1 <= nums.length <= 5000
-104 <= nums[i] <= 104
All values of nums are unique.
nums is an ascending array that is possibly rotated.
-104 <= target <= 104
"""
    # potiential edge cases:
        # only one value in the list
        # list is not rotated
        # max num times rotated? going to assume 1 for this problem

# def search(nums: list[int], target: int) -> int:
#     # everything in the left half of the array will be greater than the values in the right half
#     l, r = 0, len(nums) - 1

#     while l <= r:
#         mid = l + (r - l) // 2
#         # print(nums[mid])

#         if nums[mid] == target:
#             return mid

#         if nums[l] <= nums[mid]: # if in left sorted
#             if target > nums[mid] or target < nums[l]:
#                 l = mid + 1
#             else:
#                 r = mid - 1
#         else:  # if in right sorted
#             if target < nums[mid] or target > nums[r]:
#                 r = mid - 1
#             else:
#                 l = mid + 1

#     return -1


def search(nums: list[int], target: int) -> int:
    l, r = 0, len(nums) - 1

    while l <= r:
        mid = (r + l) // 2

        if nums[mid] == target: return mid

        if nums[l] <= nums[mid]:
            if target > nums[mid] or target < nums[l]: # discard left
                l = mid + 1
            else: # discard right
                r = mid - 1
        else:
            if target > nums[mid] or target > nums[r]: # discard right
                r = mid - 1
            else:
                l = mid + 1

    return -1

print(search([4,5,6,7,0,1,2], 0)) # 4
print(search([4,5,6,7,0,1,2], 3)) # -1
print(search([4,5,6,7,0,1,2], 4)) # 0
print(search([1], 0)) # -1
print(search([5,1,3], 5)) # 0
print(search([1,3], 3)) # 1
