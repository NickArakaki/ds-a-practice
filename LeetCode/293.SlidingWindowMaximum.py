"""
You are given an array of integers nums, there is a sliding window of size k which is
moving from the very left of the array to the very right. You can only see the
k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.
"""

# def max_sliding_window(nums: list[int], k: int) -> list[int]:
#     # create a sliding window of length k
#     l, r = 0, k
#     res = []
#     # repeat until end of array
#     while r <= len(nums):
#         # iterate through curr sub array and find max
#         max_el = max(nums[l: r])
#         # add max to res array
#         res.append(max_el)
#         l += 1
#         r += 1
#     # return res array
#     return res

from collections import deque

def max_sliding_window(nums: list[int], k: int) -> list[int]:
    # use a queue to hold indices
    queue = deque()
    res = []
    # init l and r pointers to start of nums
    l = r = 0
    # repeat until end of nums
    while r < len(nums):
        # remove values from queue if the previous val is < nums[r]
        while queue and nums[queue[-1]] < nums[r]:
            queue.pop()
        # add r to queue
        queue.append(r)

        # if l val is not part of window
        if l > queue[0]:
            # popleft
            queue.popleft()

        if r + 1 >= k:
            res.append(nums[queue[0]])
            l += 1

        r += 1

        # increment r
    return res


print(max_sliding_window([1,3,-1,-3,5,3,6,7], 3) == [3,3,5,5,6,7])
print(max_sliding_window([1], 1) == [1])
