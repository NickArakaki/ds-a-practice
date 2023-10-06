"""
Given an integer n, break it into the sum of k positive integers, where k >= 2, and maximize the product of those integers.

Return the maximum product you can get.
"""

def integer_break(n: int) -> int:
    # recursive solution
    # dfs
    # base case: if num == 1 return 1
    # initial val = 0 if current num == n else n because we need to break up n into at least 2 nums
    # iterate thru range from 1 to num, non-inclusive
        # get the product of dfs(i) * dfs(num - i)
        # set val to the max of current val and the product
    # return max val
# call dfs(n)
    # cache = {1: 1}

    # def _dfs(num) -> int:
    #     if num in cache:
    #         return cache[num]

    #     val = 0 if num == n else num
    #     for i in range(1, num):
    #         val = max(val, (_dfs(i) * _dfs(num - i)))

    #     cache[num] = val
    #     return val

    # return _dfs(n)

    # iterative, dp solution
    cache = {1: 1}
    for num in range(1, n + 1):
        val = 0 if num == n else num
        for i in range(1, num):
            val = max(val, cache[i] * cache[num - i])
        cache[num] = val
    return cache[n]


print(integer_break(2) == 1)
print(integer_break(10) == 36)
