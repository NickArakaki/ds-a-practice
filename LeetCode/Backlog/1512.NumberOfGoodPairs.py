"""
Given an array of integers nums, return the number of good pairs.

A pair (i, j) is called good if nums[i] == nums[j] and i < j.
"""
from collections import Counter

def num_identical_pairs(nums: list[int]) -> int:
    count = Counter(nums)
    pairs = 0
    for num in count:
        num_count = count[num]
        num_pairs = num_count * (num_count - 1) // 2
        pairs += num_pairs
    return pairs


print(num_identical_pairs([1,2,3,1,1,3]) == 4) # (0,3), (0,4), (3,4), (2,5)
print(num_identical_pairs([1,1,1,1]) == 6) # each pair in the array
print(num_identical_pairs([1,2,3]) == 0) # no identical pairs
