# def sansaXor(arr):
#     xor_vals = []
#     l, r = 0, 0
#     while r < len(arr) or l < len(arr):
#         if l == r:
#             xor_vals.append(arr[l])
#             r += 1
#         elif r == len(arr):
#             l += 1
#             r = l
#         else:
#             xor_vals.append(xor_vals[-1] ^ arr[r])
#             r += 1

#     res = xor_vals.pop()
#     while len(xor_vals):
#         res = res ^ xor_vals.pop()

#     return res

def sansaXor(arr):
    if len(arr) % 2 == 0:
        return 0

    res = 0
    for i in range(len(arr)):
        if i % 2 == 0:
            res ^= arr[i]

    return res


print(sansaXor([1,2,3])) # 2
print(sansaXor([3,4,5])) # 6
print(sansaXor([4,5,7,5])) # 0
