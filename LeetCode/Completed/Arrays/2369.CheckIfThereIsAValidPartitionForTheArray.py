"""
You are given a 0-indexed integer array nums. You have to partition the array into one or more contiguous subarrays.

We call a partition of the array valid if each of the obtained subarrays satisfies one of the following conditions:

The subarray consists of exactly 2 equal elements. For example, the subarray [2,2] is good.
The subarray consists of exactly 3 equal elements. For example, the subarray [4,4,4] is good.
The subarray consists of exactly 3 consecutive increasing elements, that is, the
difference between adjacent elements is 1. For example, the subarray [3,4,5] is good,
but the subarray [1,3,5] is not.
Return true if the array has at least one valid partition. Otherwise, return false.
"""

# def valid_partition(nums: list[int]) -> bool:
#     cache = {}

#     def dfs(i):
#         if i == len(nums):
#             return True

#         if i in cache:
#             return cache[i]

#         res = False

#         if i < len(nums) - 1 and nums[i] == nums[i + 1]:
#             res = dfs(i + 2)
#         if i < len(nums) - 2:
#             if (nums[i] == nums[i + 1] == nums[i + 2]) or (nums[i] + 1 == nums[i + 1] == nums[i + 2] -1):
#                 res = res or dfs(i + 3)

#         cache[i] = res
#         return res

#     return dfs(0)


# DP solution
def valid_partition(nums: list[int]) -> bool:
    two = nums[-1] == nums[-2]
    if len(nums) == 2:
        return two

    three = (nums[-1] == nums[-2] == nums[-3]) or (nums[-3] + 1 == nums[-2] == nums[-1] - 1)

    dp = [three,two,False]

    for i in range(len(nums) - 4, -1, -1):
        curr = (nums[i] == nums[i + 1]) and dp[1]
        curr = curr or ((nums[i] + 1 == nums[i + 1] == nums[i + 2] - 1 or
                        nums[i] == nums[i + 1] == nums[i + 2]) and
                        dp[2])

        dp = [curr, dp[0], dp[1]]

    return dp[0]


print(valid_partition([4,4,4,5,6]) == True)
print(valid_partition([1,1,1,2]) == False)
print(valid_partition([993335,993336,993337,993338,993339,993340,993341]) == False)
