def maxMin(k, arr):
    arr.sort()
    l,r = 0, k - 1
    min = float("inf")

    while r < len(arr):
        difference = arr[r] - arr[l]
        if difference < min: min = difference
        l += 1
        r += 1

    return min

print(maxMin(2, [1,4,7,2])) # 3
