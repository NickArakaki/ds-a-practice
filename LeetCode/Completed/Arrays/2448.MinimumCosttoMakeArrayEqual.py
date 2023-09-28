"""
You are given two 0-indexed arrays nums and cost consisting each of n positive integers.

You can do the following operation any number of times:

Increase or decrease any element of the array nums by 1.
The cost of doing one operation on the ith element is cost[i].

Return the minimum total cost such that all the elements of the array nums become equal.
"""

def minCost(nums: list[int], cost: list[int]) -> int:
    def total_cost(mid_value):
        total_cost = 0
        for i, num in enumerate(nums):
            total_cost += abs(mid_value - num) * cost[i]
        return total_cost

    l = min(nums)
    r = max(nums)

    while l < r:
        mid = (l + r) // 2
        if total_cost(mid) < total_cost(mid + 1):
            r = mid
        else:
            l = mid + 1

    return total_cost(l)

print(minCost([1,3,5,2], [2,3,1,14])) # 8
print(minCost([2,2,2,2,2], [4,2,8,1,3])) # 0
