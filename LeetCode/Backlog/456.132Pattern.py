"""
Given an array of n integers nums, a 132 pattern is a subsequence of three integers nums[i],
nums[j] and nums[k] such that i < j < k and nums[i] < nums[k] < nums[j].

Return true if there is a 132 pattern in nums, otherwise, return false.
"""

def find_132_pattern(nums: list[int]) -> bool:
    if len(nums) < 3: return False
    stack = [(nums[0], nums[0])] # i, j
    cur_min = nums[0]

    for n in nums[1:]:
        while stack and n >= stack[-1][1]:
            stack.pop()
        if stack and n > stack[-1][0]:
            return True
        stack.append((cur_min, n))
        cur_min = min(n, cur_min)

    return False


print(find_132_pattern([1,2,3,4]) == False)
print(find_132_pattern([3,1,4,2]) == True)
print(find_132_pattern([-1,3,2,0]) == True)
print(find_132_pattern([3,5,0,3,4]) == True)
