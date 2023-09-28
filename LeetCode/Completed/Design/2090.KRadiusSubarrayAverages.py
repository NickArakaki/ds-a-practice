"""
You are given a 0-indexed array nums of n integers, and an integer k.

The k-radius average for a subarray of nums centered at some index i
with the radius k is the average of all elements in nums between the indices
i - k and i + k (inclusive). If there are less than k elements before or after the index i, then the k-radius average is -1.

Build and return an array avgs of length n where avgs[i] is the k-radius
average for the subarray centered at index i.

The average of x elements is the sum of the x elements divided by x,
using integer division. The integer division truncates toward zero, which means losing its fractional part.

For example, the average of four elements 2, 3, 1, and 5 is (2 + 3 + 1 + 5) / 4 = 11 / 4 = 2.75, which truncates to 2.
"""

def getAverages(nums: list[int], k: int) -> list[int]:
    # determine if there are at least k elements on either side of mid
    if k == 0: return nums

    left_sum, right_sum = 0, sum(nums[:k + 1])
    l, r = 0, k + 1
    res = []

    for i, num in enumerate(nums):
        num_el_left = i - 0
        num_el_right = len(nums) - i - 1
        if num_el_left < k or num_el_right < k:
            res.append(-1)
        else:
            avg = (left_sum + right_sum) // (k * 2 + 1)
            res.append(avg)
            left_sum -= nums[l]
            l += 1

        if r < len(nums):
            right_sum += nums[r]
            r += 1

        left_sum += num
        right_sum -= num
    return res

print(getAverages([7,4,3,9,1,8,5,2,6], 3)) # [-1,-1,-1,5,4,4,-1,-1,-1]
print(getAverages([100000], 0)) # [100000]
print(getAverages([8], 100000)) # [-1]
print(getAverages([8, 1, 3], 1)) # [-1, 4, -1]
print(getAverages([8, 2], 100000)) # [-1, -1]
