"""
Given a sorted array of distinct integers and a target value,
return the index if the target is found. If not, return the
index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.
"""

def search_insert(nums: list[int], target: int) -> int:
    l, r = 0, len(nums) - 1

    if target > nums[-1]: return r + 1

    while l < r:
        mid = (l + r) // 2
        if nums[mid] < target:
            l = mid + 1
        else:
            r = mid

    return l

print(search_insert([1,3,5,6], 5) == 2)
print(search_insert([1,3,5,6], 2) == 1)
print(search_insert([1,3,5,6], 7) == 4)
