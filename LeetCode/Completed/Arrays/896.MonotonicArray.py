"""
An array is monotonic if it is either monotone increasing or monotone decreasing.

An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j].
An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].

Given an integer array nums, return true if the given array is monotonic, or false otherwise.
"""

def is_monotonic(nums: list[int]) -> bool:
    l = mid = 0
    while mid < len(nums) - 1 and nums[mid] == nums[l]:
        mid += 1
    r = mid
    while r < len(nums) - 1:
        while r < len(nums) - 1 and nums[mid] == nums[r]:
            r += 1
        if nums[l] > nums[mid] < nums[r] or nums[l] < nums[mid] > nums[r]:
            return False
        l = mid
        mid = r
    return True


print(is_monotonic([1,2,2,3]) == True)
print(is_monotonic([6,5,4,4]) == True)
print(is_monotonic([1,3,2]) == False)
print(is_monotonic([11,11,9,4,3,3,3,1,-1,-1,3,3,3,5,5,5]) == False)
print(is_monotonic([5,5,5,5,5,5]) == True)
print(is_monotonic([5]) == True)
print(is_monotonic([5,5]) == True)
print(is_monotonic([5,4]) == True)
