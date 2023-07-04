"""
Given an array nums of distinct integers, return all the possible permutations.
You can return the answer in any order.
"""

def permute(nums: list[int]) -> list[list[int]]:
    res = []
    if len(nums) == 1:
        return [nums.copy()]

    for _ in range(len(nums)):
        num = nums.pop(0)
        permutations = permute(nums)

        for permutation in permutations:
            permutation.append(num)

        nums.append(num)
        res.extend(permutations)

    return res

print(permute([1,2,3]) == [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]])
print(permute([0,1]) == [[0,1],[1,0]])
print(permute([1]) == [[1]])
