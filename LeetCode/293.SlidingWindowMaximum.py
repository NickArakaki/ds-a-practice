"""
You are given an array of integers nums, there is a sliding window of size k which is
moving from the very left of the array to the very right. You can only see the
k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.
"""

def max_sliding_window(nums: list[int], k: int) -> list[int]:
    pass


print(max_sliding_window([1,3,-1,-3,5,3,6,7], 3) == [3,3,5,5,6,7])
print(max_sliding_window([1], 1) == [1])
