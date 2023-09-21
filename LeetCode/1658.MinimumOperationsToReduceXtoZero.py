"""
You are given an integer array nums and an integer x. In one operation,
you can either remove the leftmost or the rightmost element from the array nums and subtract its value from x.
Note that this modifies the array for future operations.

Return the minimum number of operations to reduce x to exactly 0 if it is possible, otherwise, return -1.
"""


def min_operations(nums: list[int], x: int) -> int:
    """
    input: list of ints and target int
    output: int (min num of operations needed to reduce x to zero)
    """
    # sliding window technique
    # get total sum of nums
    # calculate target of middle (total sum - x)
    target = sum(nums) - x
    # keep track of curr sum
    curr_sum = 0
    # init l and r pointers
    l = 0
    # keep track of max window length
    max_window = -1
    for r, num in enumerate(nums):
        # add num at r to curr sum
        curr_sum += num
        # while curr_sum > target
        while l <= r and curr_sum > target:
            # decrement curr sum by num at l
            curr_sum -= nums[l]
            # incremnt l pointer
            l += 1
        # if curr_sum == target
        if curr_sum == target:
            # calculate window size
            curr_window = r - l + 1
            # update max_window size accordingly
            max_window = max(max_window, curr_window)

    return -1 if max_window == -1 else len(nums) - max_window


print(min_operations([1, 1, 4, 2, 3], 5) == 2)
print(min_operations([5, 6, 7, 8, 9], 4) == -1)
print(min_operations([3, 2, 20, 1, 1, 3], 10) == 5)
print(min_operations([1, 8, 3, 3, 3], 9) == 2)
print(min_operations([1, 1, 1, 1], 9) == -1)
