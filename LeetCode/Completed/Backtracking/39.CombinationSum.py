"""
Given an array of distinct integers candidates and a target integer target,
return a list of all unique combinations of candidates where the chosen
numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times.
Two combinations are unique if the frequency of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique
combinations that sum up to target is less than 150 combinations for the given input.
"""

def combination_sum(candidates: list[int], target: int) -> list[list[int]]:
    ans = []

    def _backtrack(i, combo, total):
        if total == target:
            ans.append(combo.copy())
            return
        if i >= len(candidates) or total > target:
            return

        # include candidates[i]
        combo.append(candidates[i])
        _backtrack(i, combo, total + candidates[i])
        combo.pop()

        # exclude candidates[i]
        _backtrack(i + 1, combo, total)

    _backtrack(0, [], 0)
    return ans


print(combination_sum([2,3,6,7], 7)) # [[2,2,3],[7]]
# print(combination_sum([2,3,5], 8)) # [[2,2,2,2],[2,3,3],[3,5]]
# print(combination_sum([2], 1)) # []
print(combination_sum([7,3,2], 18)) # [[7,7,2,2],[7,3,3,3,2],[7,3,2,2,2,2],[3,3,3,3,3,3],[3,3,3,3,2,2,2],[3,3,2,2,2,2,2,2],[2,2,2,2,2,2,2,2,2]]
# print(len(combination_sum([7,3,2], 18)) == 7)
