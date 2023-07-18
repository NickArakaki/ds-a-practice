"""
Given two strings s and t,
return true if t is an anagram of s,
and false otherwise.

An Anagram is a word or phrase
formed by rearranging the letters of
a different word or phrase, typically
using all the original letters exactly once.

Constraints:
    1 <= s.length, t.length <= 5 * 104

    s and t consist of lowercase English letters.
"""

def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t): return False

    s_chars, t_chars = {}, {}

    for i in range(len(s)):
        if s[i] not in s_chars:
            s_chars[s[i]] = 1
        else:
            s_chars[s[i]] += 1

        if t[i] not in t_chars:
            t_chars[t[i]] = 1
        else:
            t_chars[t[i]] += 1

    # for char in s_chars:
    #     if (char not in t_chars) or (s_chars[char] != t_chars[char]):
    #         return False

    return s_chars == t_chars

print(isAnagram("anagram", "nagaram")) # True
print(isAnagram("rat", "car")) # False
