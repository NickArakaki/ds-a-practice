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
    candidates.sort()

    def _backtrack(combo):
        if sum(combo) == target:
            combo.sort()
            if combo not in ans:
                ans.append(combo[::])
            return
        if sum(combo) > target:
            return

        i = 0
        while i < len(candidates):

            # decision to add
            combo.append(candidates[i])
            _backtrack(combo)
            combo.pop()
            i += 1
            # decision to not add
            # _backtrack(combo)

    _backtrack([])
    return ans


# print(combination_sum([2,3,6,7], 7)) # [[2,2,3],[7]]
# print(combination_sum([2,3,5], 8)) # [[2,2,2,2],[2,3,3],[3,5]]
# print(combination_sum([2], 1)) # []
print(combination_sum([7,3,2], 18)) # [[7,7,2,2],[7,3,3,3,2],[7,3,2,2,2,2],[3,3,3,3,3,3],[3,3,3,3,2,2,2],[3,3,2,2,2,2,2,2],[2,2,2,2,2,2,2,2,2]]
# print(len(combination_sum([7,3,2], 18)) == 7)
