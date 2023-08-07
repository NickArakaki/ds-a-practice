"""
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.
"""

def reverse_vowels(s: str) -> str:
    vowels = {"a", "e", "i", "o", "u"}
    chars = [*s]
    l, r = 0, len(chars) - 1

    while l < r:
        while chars[l] not in vowels:
            l += 1
        while chars[r] not in vowels:
            r -=1

        if l < r:
            chars[l], chars[r] = chars[r], chars[l]
            l += 1
            r -=1

        # if chars[l] not in vowels:
        #     l += 1
        # if chars[r] not in vowels:
        #     r -= 1
        # if chars[l] in vowels and chars[r] in vowels:
        #     chars[l], chars[r] = chars[r], chars[l]
        #     l += 1
        #     r -= 1

    return "".join(chars)



print(reverse_vowels("hello") == "holle")
print(reverse_vowels("leetcode") == "leotcede")
print(reverse_vowels("cdf") == "cdf")
