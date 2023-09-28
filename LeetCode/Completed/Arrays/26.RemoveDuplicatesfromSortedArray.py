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
    l = r = 0
    # iterate thru nums with l and r pointers
    while l < len(nums) and r < len(nums):
        # if nums[l] in seen_nums:
        if nums[l] in seen_nums:
            # move r pointer to first number not in nums or until end of nums
            while r < len(nums) and nums[r] in seen_nums:
                r += 1

            # if nums[r] not in seen_nums
                # swap nums[l] and nums[r]
            if r < len(nums) and nums[r] not in seen_nums:
                nums[l], nums[r] = nums[r], nums[l]
        seen_nums.add(nums[l])
        l += 1
        r += 1
        # add nums[l] to seen_nums
        # increment l and r pointers
    # return length of seen_nums set
    return len(seen_nums)

print(remove_duplicates([0,0,1,1,1,2,2,3,3,4]) == 5)
print(remove_duplicates([1,1,2]) == 2)
print(remove_duplicates([1,1,1]) == 1)
print(remove_duplicates([1]) == 1)
