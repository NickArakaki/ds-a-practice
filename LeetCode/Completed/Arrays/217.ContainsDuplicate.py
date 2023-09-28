"""
Given an integer array nums,
return true if any value appears
at least twice in the array,
and return false if every element is distinct.
"""

def containsDuplicate(nums):
    seen_nums = set()

    for num in nums:
        if num in seen_nums: return True
        seen_nums.add(num)

    return False


print(containsDuplicate([1,2,3,1])) # True
print(containsDuplicate([1,2,3,4])) # False
print(containsDuplicate([1,1,1,3,3,4,3,2,4,2])) # False
