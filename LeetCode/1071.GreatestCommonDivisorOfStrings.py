"""
For two strings s and t, we say "t divides s" if and only if s = t + ... + t
(i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.
"""

def gcd_of_strings(str1: str, str2: str) -> str:
    if str1 + str2 != str2 + str1:
        return ""

    if len(str1) < len(str2):
        str1, str2 = str2, str1

    return str1[:gcd(len(str1), len(str2))]


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

print(gcd_of_strings('ABCABC', 'ABC') == 'ABC')
print(gcd_of_strings('ABABAB', 'ABAB') == 'AB')
print(gcd_of_strings('LEET', 'CODE') == '')
