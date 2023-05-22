"""
A peak element is an element that is strictly greater than its neighbors.

Given a 0-indexed integer array nums, find a peak element,
and return its index. If the array contains multiple peaks,
return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞. In other words,
an element is always considered to be strictly greater than a
neighbor that is outside the array.

You must write an algorithm that runs in O(log n) time.

Constraints

1 <= nums.length <= 1000
-231 <= nums[i] <= 231 - 1
nums[i] != nums[i + 1] for all valid i.
"""

def findPeakElement(nums:list[int]) -> int:
    l, r = 0, len(nums) - 1

    while l <= r:
        mid = l + (r - l) // 2
        if mid > 0 and nums[mid] < nums[mid - 1]: # search left
            r = mid - 1
        elif mid < len(nums) - 1 and nums[mid] < nums[mid + 1]: # search right
            l = mid + 1
        else:
            return mid

print(findPeakElement([1,2,3,1])) # 2
print(findPeakElement([1,2,1,3,5,6,4])) # 5
