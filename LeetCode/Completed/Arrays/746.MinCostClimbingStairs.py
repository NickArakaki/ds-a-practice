"""
You are given an integer array cost where cost[i] is the cost of ith step on a staircase.
Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.
"""

def min_cost_climbing_stairs(cost: list[int]) -> int:
    dp = [0,0]
    for i in range(2, len(cost) + 1):
        dp.append(min(cost[i - 1] + dp[-1], cost[i - 2] + dp[-2]))

    return dp[-1]


print(min_cost_climbing_stairs([10,15,20]) == 15)
print(min_cost_climbing_stairs([1,100,1,1,1,100,1,1,100,1]) == 6)
