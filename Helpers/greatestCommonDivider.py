# def greatestCommonDivider(a: int, b: int) -> int:
#     if b == 0:
#         return a

#     a, b = b, a % b
#     return greatestCommonDivider(a, b)

# iterative GCD
def greatestCommonDivider(a: int, b: int) -> int:
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a

def getGCDList(nums: list[int]) -> int:
    res = nums[0]
    for num in nums[1:]:
        res = greatestCommonDivider(res, num)

    return res

print(greatestCommonDivider(2000, 500)) # 2
print(getGCDList([3])) # 1
