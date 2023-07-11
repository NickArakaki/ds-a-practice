"""
Given a sorted array of distinct integers and a target value,
return the index if the target is found. If not, return the
index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.
"""

def search_insert(nums: list[int], target: int) -> int:
    l, r = 0, len(nums) - 1
    mid = 0

    while l <= r:
        mid = (l + r) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            r = mid
        else:
            l = mid + 1

    return mid

print(search_insert([1,3,5,6], 5) == 2)
print(search_insert([1,3,5,6], 2) == 1)
print(search_insert([1,3,5,6], 7) == 4)
