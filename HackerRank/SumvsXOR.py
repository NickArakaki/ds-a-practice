def sumXor(n):
    num_equal = 0

    for i in range(n + 1):
        num_sum = n + i
        num_xor = n ^ i
        if num_sum == num_xor:
            num_equal += 1

    return num_equal

print(sumXor(5)) # 2
print(sumXor(10)) # 4
