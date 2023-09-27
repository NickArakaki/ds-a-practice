"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
"""

def three_sum(nums: list[int]) -> list[list[int]]:
    # init a res array
    res = []
    # init seen set
    seen = set()
    # iterate through nums
    for i, num in enumerate(nums):
        if num not in seen:
            seen.add(num)
            # get difference between 0 and num
            target = 0 - num
            # pass remaining nums to two sum helper with difference as the target
            combos = two_sum(nums[i:], target)
            # iterate thru returned list
            for combo in combos:
                # add num to each sublist
                combo.append(num)
                # append sublist to res
                res.append(combo)
    # return res
    return res

def two_sum(nums: list[int], target: int) -> list[list[int]]:
    # init a hashmap diff between num and target as key, val is num
    # init res list
    # iterate through nums
        # calculate diff
        # if diff in hashmap
            #
    # return res list
    pass

print(three_sum([-1,0,1,2,-1,-4]) == [[-1,-1,2],[-1,0,1]])
print(three_sum([]) == [])
print(three_sum([0,0,0]) == [[0,0,0]])
