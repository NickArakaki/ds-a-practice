"""
Sherlock considers a string to be valid if all characters of the string appear the same number of times.
It is also valid if he can remove just  character at  index in the string, and the remaining characters will occur
the same number of times. Given a string , determine if it is valid. If so, return YES, otherwise return NO.
"""

def is_valid(s: str) -> str:
    pass

print(is_valid("abcdefghhgfedecba") == "YES")
print(is_valid("aabbcd") == "NO")
print(is_valid("aabbccddeefghi") == "NO")
