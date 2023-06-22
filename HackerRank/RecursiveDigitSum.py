def superDigit(n,k):
    super_dig = sum([int(s) for s in n]) * k
    if super_dig < 10:
        return super_dig
    else:
        return superDigit(str(super_dig), 1)

print(superDigit('9875', 4)) # 8
print(superDigit('148', 3)) # 3
print(superDigit('123', 3)) # 9
