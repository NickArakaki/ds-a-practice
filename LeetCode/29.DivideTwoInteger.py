"""
Given two integers dividend and divisor, divide two integers without using multiplication,
division, and mod operator.

The integer division should truncate toward zero, which means losing its fractional
part. For example, 8.345 would be truncated to 8, and -2.7335 would be truncated to -2.

Return the quotient after dividing dividend by divisor.

Note: Assume we are dealing with an environment that could only store integers within the
32-bit signed integer range: [−231, 231 − 1]. For this problem, if the quotient is strictly
greater than 231 - 1, then return 231 - 1, and if the quotient is strictly less than -231, then return -231.
"""

def divide(dividend: int, divisor: int) -> int:
    ans = 0
    val = 0
    while val <= abs(dividend):
        val += abs(divisor)
        ans += 1
    ans -= 1

    if (divisor < 0 and dividend > 0) or (divisor > 0 and dividend < 0):
        ans = 0 - ans
    return ans

print(divide(10, 3)) # 3
print(divide(7, -3)) # -2
print(divide(0, -3)) # 0
print(divide(1, 1)) # 1
