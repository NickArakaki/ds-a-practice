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
    pass


print(min_operations([1, 1, 4, 2, 3], 5) == 2)
print(min_operations([5, 6, 7, 8, 9], 4) == -1)
print(min_operations([3, 2, 20, 1, 1, 3], 10) == 5)
print(min_operations([1, 8, 3, 3, 3], 9) == 2)
