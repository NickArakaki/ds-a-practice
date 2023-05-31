def birthday(s, d, m):
    # Write your code here
    if len(s) < m:
        return 0

    l, r = 0, m
    # initialize a sum var
    total = sum(s[:m])
    # initialize a count var to 0
    count = 1 if total == d else 0

    while r < len(s):
        total = total - s[l] + s[r]
        l += 1
        r += 1
        if total == d:
            count += 1
    return count

print(birthday([4], 4, 1)) # 1
print(birthday([1,2,1,3,2], 3, 2)) # 2
print(birthday([1,1,1,1,1,1], 3, 2)) # 0
