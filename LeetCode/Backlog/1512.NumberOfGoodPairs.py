"""
Given an array of integers nums, return the number of good pairs.

A pair (i, j) is called good if nums[i] == nums[j] and i < j.
"""

def num_identical_pairs(nums: list[int]) -> int:
    # count each el of nums
    # iterate thru keys of count
        # calculate num pairs for each count n(n-1) / 2
    # return num pairs
    pass


print(num_identical_pairs([1,2,3,1,1,3]) == 4) # (0,3), (0,4), (3,4), (2,5)
print(num_identical_pairs([1,1,1,1]) == 6) # each pair in the array
print(num_identical_pairs([1,2,3]) == 0) # no identical pairs
