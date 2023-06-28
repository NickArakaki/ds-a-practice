def subsets(nums: list[int]) -> list[list[int]]:
    ans = []
    subset = []

    def _backtrack(i):
        if i >= len(nums):
            ans.append([*subset])
            return

        # exclude nums[i]
        _backtrack(i+1)

        # include nums[i]
        subset.append(nums[i])
        _backtrack(i+1)
        subset.pop()

    _backtrack(0)

    return ans

print(subsets([1,2,3])) # [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
print(subsets([0])) # [[], [0]]
