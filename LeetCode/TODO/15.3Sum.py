"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
"""

# def three_sum(nums: list[int]) -> list[list[int]]:
#     # sort nums
#     nums.sort()
#     # init a res array
#     res = []
#     # init seen set
#     seen = set()
#     # iterate through nums
#     for i, num in enumerate(nums):
#         if num not in seen:
#             seen.add(num)
#             # get difference between 0 and num
#             target = 0 - num
#             # pass remaining nums to two sum helper with difference as the target
#             combos = two_sum(nums[i:], target)
#             # iterate thru returned list
#             for combo in combos:
#                 # add num to each sublist
#                 combo.append(num)
#                 # append sublist to res
#                 res.append(combo)
#     # return res
#     return res

# def two_sum(nums: list[int], target: int) -> list[list[int]]:
#     # init a hashmap diff num:bool
#     num_map = {}
#     # init res list
#     res = []
#     # iterate through nums
#     for num in nums:
#         # calculate diff
#         diff = target - num
#         # if diff in hashmap and has not been used
#         if diff in num_map and not num_map[diff]:
#             # add current num and map[diff], to res list as list
#             res.append([diff, num])
#             # map[diff] = True
#             num_map[diff] = True
#         num_map[num] = False
#     # return res list
#     return res

def three_sum(nums: list[int]) -> list[list[int]]:
    # sort nums
    nums.sort()
    # init res list
    res = []
    # iterate over sorted nums
    for i, num in enumerate(nums):
        if i > 0 and num == nums[i - 1]:
            continue
        l, r = i + 1, len(nums) - 1
        while l < r:
            cur_sum = num + nums[l] + nums[r]
            if cur_sum > 0:
                # move right pointer to left
                r -= 1
            elif cur_sum < 0:
                # move left pointer to right
                l += 1
            else:
                # add current combo to res list
                res.append([num, nums[l], nums[r]])
                # increment left pointer
                l += 1
                # while left == nums[left-1] and left < right:
                while nums[l] == nums[l - 1] and l < r:
                    # increment left
                    l += 1
    return res

print(three_sum([-1,0,1,2,-1,-4]) == [[-1,-1,2],[-1,0,1]])
print(three_sum([]) == [])
print(three_sum([0,0,0]) == [[0,0,0]])
