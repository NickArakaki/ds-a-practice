"""
You are given two 0-indexed integer arrays nums and multipliers of size n and m respectively, where n >= m.

You begin with a score of 0. You want to perform exactly m operations. On the ith operation (0-indexed) you will:

Choose one integer x from either the start or the end of the array nums.
Add multipliers[i] * x to your score.
Note that multipliers[0] corresponds to the first operation, multipliers[1] to the second operation, and so on.
Remove x from nums.
Return the maximum score after performing m operations.
"""

def max_score(nums: list[int], multiplier: list[int]) -> int:
    pass


print(max_score([1,2,3], [3,2,1]))
print(max_score([-5,-3,-3,-2,7,1], [-10,-5,3,4,6]))
