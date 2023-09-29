"""
An array is monotonic if it is either monotone increasing or monotone decreasing.

An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j].
An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].

Given an integer array nums, return true if the given array is monotonic, or false otherwise.
"""

def is_monotonic(nums: list[int]) -> bool:
    # three pointers
    # init l pointer to 0
    # init r and mid to 0
    # iterate while r < len nums
    # mid = next el that is not equal to nums[l]
    # r = next el that is not equal to nums[mid]
    # if nums[l] > nums[mid] < nums[r] or nums[l] < nums[mid] > nums[r]:
        # return False
    # l points to mid
    # mid points to r
    # return True
    pass


print(is_monotonic([1,2,2,3]) == True)
print(is_monotonic([6,5,4,4]) == True)
print(is_monotonic([1,3,2]) == False)
print(is_monotonic([11,11,9,4,3,3,3,1,-1,-1,3,3,3,5,5,5]) == False)
