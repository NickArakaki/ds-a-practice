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
    memo = {}
    # backtracking
    def _backtrack(num_l, num_r, mult_i, cur_sum: int=0) -> int:
        if mult_i >= len(multipliers):
            return cur_sum

        if (num_l, num_r, mult_i) in memo:
            return memo[(num_l, num_r, mult_i)]

        max_sum = cur_sum

        # take l num
        cur_sum += nums[num_l] * multipliers[mult_i]
        max_sum = max(max_sum, _backtrack(num_l + 1, num_r, mult_i + 1, cur_sum))

        # backtrack
        cur_sum -= nums[num_l] * multipliers[mult_i]

        # take r num
        cur_sum += nums[num_r] * multipliers[mult_i]
        max_sum = max(max_sum, _backtrack(num_l, num_r - 1, mult_i + 1, cur_sum))

        memo[(num_l, num_r, mult_i)] = max_sum
        return max_sum

    return _backtrack(0, len(nums) - 1, 0)


print(max_score([1,2,3], [3,2,1]) == 14)
print(max_score([-5,-3,-3,-2,7,1], [-10,-5,3,4,6]) == 102)
print(max_score([-5,-3,-3,-2,7,1], [-10,-5]) == 65)
print(max_score([830,388,289,14,-221,610,163,444,-750,-217,-235,-882,746,-907,67,-71,-990,400,-54,-114,-100,233,667,612,
                 -812,-471,-639,-306,-95,524,-198,-520,-652,704,-697,-43,-539,-105,-160,838,499,-109,-977,975,658,-250,
                 593,154,-777,496,747,307,-340,403,-749,-185,721,327,-851,-112,770,-14,754,-242,-220,-776,-66,348,-707,
                 -693,9,-354,741,129,234,638,404,-408,-30,422,-234,818,-627,706,-752,-699,-773,-786,241,432,273,272,-57,
                 878,-149,-547,491,519,870,700,476,-99,902,-878,-237,-549,445,-372,277,-486,872,-569,-687,339,653,-564,
                 862,898,-962,306,668,-143,344,-312,108,-536,-453,-52,627,-225,-28,403,-422,367,133,970,-575,353,347,275,
                 -876,337,594,441,-498,-875,-934,133],
                [-844,-363,797,480,141,733,-935,842,160,-928,787,-895,-742,-963,889,-713,-264,-400,117,163,68,-286,-810,
                 -365,180,-690,-558,-409,290,51,-272,-454,-110,850,578,131,-913,675,817,380,410,860,-441,56,-80,-650,-474,
                 858,269]) == 11042056)
