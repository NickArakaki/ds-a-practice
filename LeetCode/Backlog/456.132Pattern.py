"""
Given an array of n integers nums, a 132 pattern is a subsequence of three integers nums[i],
nums[j] and nums[k] such that i < j < k and nums[i] < nums[k] < nums[j].

Return true if there is a 132 pattern in nums, otherwise, return false.
"""

def find_132_pattern(nums: list[int]) -> bool:
    # if len nums < 3 return false
    # use a stack to keep track of max and mins
    # init stack with tup (num[0], num[0]) -> i, j
    # iterate thru nums (start from 1 -> end)
        # pop from stack while cur num > max seen prior
        # check if nums[i] < nums[k] < nums[j]
        # add cur num, and min prev to stack
    # return False
    pass

# print(find_132_pattern([1,2,3,4]) == False)
# print(find_132_pattern([3,1,4,2]) == True)
# print(find_132_pattern([-1,3,2,0]) == True)
print(find_132_pattern([3,5,0,3,4]) == True)
