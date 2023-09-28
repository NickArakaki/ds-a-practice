"""
You are given an integer array coins representing coins of different
denominations and an integer amount representing a total amount of money.

Return the number of combinations that make up that amount.
If that amount of money cannot be made up by any combination of the coins, return 0.

You may assume that you have an infinite number of each kind of coin.

The answer is guaranteed to fit into a signed 32-bit integer.
"""

def change(amount: int, coins: list[int]) -> int:
    memo = set()
    res = []
    total = 0

    def _backtrack(change: list[int], coins: list[int]) -> int:
        if total == amount:
            res.append(change)

    pass


print(change(5, [1,2,5]))
print(change(3, [2]))
print(change(10, [10]))
