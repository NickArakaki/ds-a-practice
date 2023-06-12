"""
You are given a sorted unique integer array nums.

A range [a,b] is the set of all integers from a to b (inclusive).

Return the smallest sorted list of ranges that cover all the numbers
in the array exactly. That is, each element of nums is covered by exactly
one of the ranges, and there is no integer x such that x is in one of
the ranges but not in nums.

Each range [a,b] in the list should be output as:

"a->b" if a != b
"a" if a == b
"""

def summaryRanges(nums: list[int]) -> list[str]:
        if not len(nums): return []

        l = r = 0
        res = []
        while r < len(nums) - 1:
            if nums[r + 1] != nums[r] + 1:
                if l == r:
                      res.append(f"{nums[l]}")
                else:
                      res.append(f"{nums[l]}->{nums[r]}")
                r += 1
                l = r
            else:
                  r += 1
        if l == r:
              res.append(f"{nums[l]}")
        else:
              res.append(f"{nums[l]}->{nums[r]}")

        return res

print(summaryRanges([0,1,2,4,5,7])) # ["0->2","4->5","7"]
print(summaryRanges([0,1,2,4,5,7, 9])) # ["0->2","4->5","7","9"]
print(summaryRanges([0,2,3,4,6,8,9])) # ["0","2->4","6","8->9"]
print(summaryRanges([])) # []
