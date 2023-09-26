"""
Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is
the smallest in lexicographical order among all possible results.
"""

def remove_duplicate_letters(s: str) -> str:

    return s


print(remove_duplicate_letters("bcabc") == "abc")
print(remove_duplicate_letters("cbacdcbc") == "acdb")
print(remove_duplicate_letters("a") == "a")
