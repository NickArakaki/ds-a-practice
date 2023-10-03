"""
Given an array of integers nums, return the number of good pairs.

A pair (i, j) is called good if nums[i] == nums[j] and i < j.
"""
from collections import Counter

def num_identical_pairs(nums: list[int]) -> int:
    num_count = Counter(nums)
    pairs = 0
    for count in num_count.values():
        pairs += count * (count - 1) // 2
    return pairs


print(num_identical_pairs([1,2,3,1,1,3]) == 4) # (0,3), (0,4), (3,4), (2,5)
print(num_identical_pairs([1,1,1,1]) == 6) # each pair in the array
print(num_identical_pairs([1,2,3]) == 0) # no identical pairs
