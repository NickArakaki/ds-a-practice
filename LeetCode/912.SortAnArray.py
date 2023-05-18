"""
Given an array of integers nums, sort the array in
ascending order and return it.

You must solve the problem without using any built-in
functions in O(nlog(n)) time complexity and with the
smallest space complexity possible.

Constraints:
    1 <= nums.length <= 5 * 104
    -5 * 104 <= nums[i] <= 5 * 104
"""

def sortArray(nums):
    if len(nums) <= 1: # base case
        return nums

    midpoint = len(nums) // 2

    left = sortArray(nums[:midpoint])
    right = sortArray(nums[midpoint:])

    return merge(left, right)


def merge(arr1, arr2):
    res = []

    idx1, idx2 = 0, 0

    while idx1 < len(arr1) and idx2 < len(arr2):
        # compare the values at each position
        if arr1[idx1] < arr2[idx2]:
            res.append(arr1[idx1])
            idx1 += 1
        else:
            res.append(arr2[idx2])
            idx2 += 1

    if idx1 < len(arr1):
        res.extend(arr1[idx1:])

    if idx2 < len(arr2):
        res.extend(arr2[idx2:])

    return res

print(sortArray([5,2,3,1])) # [1,2,3,4,5]
print(sortArray([5,1,1,2,0,0])) # [0,0,1,1,2,5]
