def pickingNumbers(a: list[int]) -> int:
    a.sort()
    l, r = 0, 0
    max_length = 0

    while r < len(a):
        while abs(a[r] - a[l]) > 1:
            l += 1

        curr_length = r - l + 1
        max_length = max(curr_length, max_length)
        r += 1

    return max_length


print(pickingNumbers([1,2,2,3,1,2])) # 5
print(pickingNumbers([4,5,6,3,3,1])) # 3
