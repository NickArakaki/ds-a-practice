"""
Consider 2 arrays a and b where each consists of n integers
In one operation:
    1. Select two indices i and j (0 <= i, j < n)
    2. Swap integers a[i] and b[j]

This operation can be performed at most k times

Find the max number of distinct elements that can be
achieved in array a after most k operations

Example:

n = 5
a = [2,3,3,2,2]
b = [1,3,2,4,1]
k = 2

To get the maximum number of distinct elements in array a:
select i = 2, j = 0. Swap a[2] and b[0] => a = [2,3,1,2,2], b = [3,3,2,4,1]
select i = 4, j = 3
"""

def max_distinct_el(a: list[int], b: list[int], k:int) -> int:
    a_set = set(a)
    b_set = set(b)

    for b_num in b_set:
        if len(a_set) == len(a):
            return len(a)

        if k > 0 and b_num not in a_set:
            a_set.add(b_num)
            k -= 1

    return len(a_set)


print(max_distinct_el([2,3,3,2,2], [1,3,2,4,1], 2)) # 4
