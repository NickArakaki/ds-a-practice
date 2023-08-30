"""
Given an integer array nums sorted in non-decreasing order, remove the duplicates
in-place such that each unique element appears only once. The relative order of
the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique
elements in the order they were present in nums initially. The remaining elements
of nums are not important as well as the size of nums.
Return k.
"""

def remove_duplicates(nums: list[int]) -> int:
    # init seen set
    seen_nums = set()

    # l and r pointers
    # iterate thru nums with l and r pointers
        # if nums[l] in seen_nums:
            # move r pointer to first number not in nums or until end of nums
            # if r >= len(nums):
                # break
            # elif nums[r] not in seen_nums
                # swap nums[l] and nums[r]
        # add nums[l] to seen_nums
        # increment l and r pointers
    #
    # return length of seen_nums set

print(remove_duplicates([0,0,1,1,1,2,2,3,3,4]) == [0,1,2,3,4])
print(remove_duplicates([1,1,2]) == [1,2])
