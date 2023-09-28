"""
You are given an m x n binary matrix mat of 1's (representing soldiers) and 0's (representing civilians).
The soldiers are positioned in front of the civilians. That is, all the 1's will appear to the left of all the 0's in each row.

A row i is weaker than a row j if one of the following is true:

1) The number of soldiers in row i is less than the number of soldiers in row j.
2) Both rows have the same number of soldiers and i < j.

Return the indices of the k weakest rows in the matrix ordered from weakest to strongest.
"""

from collections import defaultdict
from heapq import heapify, nsmallest

# def k_weakest_rows(mat: list[list[int]], k: int) -> list[int]:
#     def _count_soldiers(row: list) -> int:
#         """
#             helper func to get num 1s in row using modified bin search
#             takes in list
#             returns int (idx of first 0)
#         """
#         # init l and r pointers
#         l, r = 0, len(row) - 1
#         # while l < r
#         while l <= r:
#             # calc mid
#             mid = (l + r) // 2
#             el = row[mid]
#             # if el at mid == 0 and el before mid is valid and not 0, we found the first 0
#             if (el == 0 and mid == 0) or (el == 0 and row[mid - 1] == 1):
#                 return mid
#             # elif el at mid == 0 and el before is also 0, search left half
#             elif el == 0 and row[mid - 1] == 0:
#                 r = mid - 1
#             # else search right
#             elif el == 1:
#                 l = mid + 1
#         # if we we exit loop without returning, it's all 1s
#         return len(row)

#     # use a dict to cache helper func results
#         # key = num 1s
#         # val = list of indices
#     cache = defaultdict(list)

#     # iterate thru matrix rows
#     for i, row in enumerate(mat):
#         num_soldiers = _count_soldiers(row)
#         cache[num_soldiers].append(i)

#     res = []
#     # iterate thru keys (0 -> n)
#     for i in range(len(mat[0]) + 1):
#         rows = cache[i]
#         for row in rows:
#             if len(res) == k:
#                 return res
#             res.append(row)
#     return res


def k_weakest_rows(mat: list[list[int]], k: int) -> list[int]:
    def _count_soldiers(row: list) -> int:
        """
            helper func to get num 1s in row using modified bin search
            takes in list
            returns int (idx of first 0)
        """
        # init l and r pointers
        l, r = 0, len(row) - 1
        # while l < r
        while l <= r:
            # calc mid
            mid = (l + r) // 2
            el = row[mid]
            # if el at mid == 0 and el before mid is valid and not 0, we found the first 0
            if (el == 0 and mid == 0) or (el == 0 and row[mid - 1] == 1):
                return mid
            # elif el at mid == 0 and el before is also 0, search left half
            elif el == 0 and row[mid - 1] == 0:
                r = mid - 1
            # else search right
            elif el == 1:
                l = mid + 1
        # if we we exit loop without returning, it's all 1s
        return len(row)

    queue = [(_count_soldiers(row), i) for i, row in enumerate(mat)]
    heapify(queue)
    return [i for _, i in nsmallest(k, queue)]


print(k_weakest_rows([
    [1,1,0,0,0],
    [1,1,1,1,0],
    [1,0,0,0,0],
    [1,1,0,0,0],
    [1,1,1,1,1]
 ], 3) == [2, 0, 3])

print(k_weakest_rows([
    [1,0,0,0],
    [1,1,1,1],
    [1,0,0,0],
    [1,0,0,0]
 ], 2) == [0,2])

print(k_weakest_rows([[1,1,1,1,1,1],[1,1,1,1,1,1],[1,1,1,1,1,1]], 1) == [0])

print(k_weakest_rows([[1,0],[1,0],[1,0],[1,1]], 4) == [0,1,2,3])
