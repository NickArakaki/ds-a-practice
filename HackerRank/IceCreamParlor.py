def icecream_parlor(m, arr):
    complements = {}

    for i, num in enumerate(arr):
        diff = m - num
        if num in complements:
            return [complements[num] + 1, i + 1]
        else:
            complements[diff] = i


print(icecream_parlor(6, [1,3,4,5,6]) == [1, 4])
print(icecream_parlor(4, [2, 2,4, 3]) == [1, 2])
