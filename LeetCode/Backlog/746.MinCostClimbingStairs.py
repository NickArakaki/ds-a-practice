"""
You are given an integer array cost where cost[i] is the cost of ith step on a staircase.
Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.
"""

def min_cost_climbing_stairs(cost: list[int]) -> int:
    # use a dp list to calculate the min cost to climb to that position
        # init list [0, 0] -> no initial cost
        # iterate through 2 -> end of list
        # min cost to reach current stair = min(cost[-1] + total_cost[-1], cost[-2] + total_cost[-2])
        # add to total_cost[i]
    # return the min(total_cost[-1], total_cost[-2])
    pass


print(min_cost_climbing_stairs([10,15,20]) == 15)
print(min_cost_climbing_stairs([1,100,1,1,1,100,1,1,100,1]) == 6)
