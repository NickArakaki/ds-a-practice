def greatestCommonDivider(a: int, b: int) -> int:
    if b == 0:
        return a

    a, b = b, a % b
    return greatestCommonDivider(a, b)

def getGCDList(nums: list[int]) -> int:
    res = nums[0]
    for num in nums[1:]:
        res = greatestCommonDivider(res, num)

    return res

print(greatestCommonDivider(2,4)) # 2
print(getGCDList([3, 5, 9])) # 4
