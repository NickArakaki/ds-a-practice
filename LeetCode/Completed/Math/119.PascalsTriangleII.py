"""
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
"""

# def get_row(rowIndex: int) -> list[int]:
#     prev = cur = [1]
#     while len(prev) < rowIndex + 1:
#         for i in range(len(prev) - 1):
#             new_val = prev[i] + prev[i + 1]
#             cur.append(new_val)
#         cur.append(1)
#         prev = cur
#         cur = [1]
#     return prev


def get_row(rowIndex: int) -> list[int]:
    res = [1]
    for i in range(1, rowIndex + 1):
        next_val = res[i - 1] * (rowIndex - i + 1) // i
        res.append(next_val)
    return res



print(get_row(3) == [1,3,3,1])
print(get_row(0) == [1])
print(get_row(1) == [1,1])
