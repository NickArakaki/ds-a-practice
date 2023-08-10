"""
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).
"""

# def pow(x: float, n: int) -> float:
#     ans = 1

#     for _ in range(abs(n)):
#         ans *= x

#     return ans if n > 0 else 1 / ans

# def pow(x: float, n: int) -> float:
#     ans = my_pow(x, abs(n))

#     return ans if n > 0 else 1 / ans


# def my_pow(x: float, n: int) -> float:
#     if n == 0:
#         return 1

#     temp = my_pow(x, n // 2)
#     temp *= temp

#     return temp if n % 2 == 0 else temp * x


def my_pow(x: float, n: int) -> float:
    if n == 0:
        return 1

    ans = solve(x, abs(n))

    return ans if n > 0 else 1 / ans


def solve(x: float, n: int) -> float:
    ans = 1

    while n > 0:
        if n & 1: # odd
            ans *= x
        x *= x
        n //= 2
    return ans


print(pow(2.00000, 10)) # 1024.00000
print(pow(2.10000, 3)) # 9.26100
print(pow(2.00000, -2)) #  0.25000
