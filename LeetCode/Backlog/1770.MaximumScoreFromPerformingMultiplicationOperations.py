"""
You are given two 0-indexed integer arrays nums and multipliers of size n and m respectively, where n >= m.

You begin with a score of 0. You want to perform exactly m operations. On the ith operation (0-indexed) you will:

Choose one integer x from either the start or the end of the array nums.
Add multipliers[i] * x to your score.
Note that multipliers[0] corresponds to the first operation, multipliers[1] to the second operation, and so on.
Remove x from nums.
Return the maximum score after performing m operations.
"""
    # parameters: nums, multipliers, cur_sum
        # max_sum = cur_sum
        # base case, if multipliers is none return cur sum
        # increment cur_sum by multiplier and left num
        # recursively call passing in nums from 1 -> end, multipliers 1 -> end, cur_sum
        # update max sum to either cur max or val returned from recursive call
        # backtrack step, undo cur_sum incrementation
        # repeat for r num
        # return max sum
    # return call backtrack passing nums, and multipliers


def max_score(nums: list[int], multipliers: list[int]) -> int:
    # backtracking
    def _backtrack(nums: list[int], multipliers: list[int], cur_sum: int=0) -> int:
        if not multipliers:
            return cur_sum

        max_sum = cur_sum

        # take l num
        cur_sum += nums[0] * multipliers[0]
        max_sum = max(max_sum, _backtrack(nums[1:], multipliers[1:], cur_sum))

        # backtrack
        cur_sum -= nums[0] * multipliers[0]

        # take r num
        cur_sum += nums[-1] * multipliers[0]
        max_sum = max(max_sum, _backtrack(nums[:-1], multipliers[1:], cur_sum))

        return max_sum

    return _backtrack(nums, multipliers)


print(max_score([1,2,3], [3,2,1]) == 14)
print(max_score([-5,-3,-3,-2,7,1], [-10,-5,3,4,6]) == 102)
