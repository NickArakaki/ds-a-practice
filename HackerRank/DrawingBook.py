import math

def pageCount(n, p):
    flip_from_front = p // 2

    if n % 2 == 0:
        flip_from_back = (n - p + 1) // 2
    else:
        flip_from_back = (n - p) // 2

    return min(flip_from_back, flip_from_front)

print(pageCount(5,4)) # 0
print(pageCount(6,2)) # 1
