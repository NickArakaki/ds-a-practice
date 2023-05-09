"""
Given a string s, find the length of the longest
substring
without repeating characters.

Constraints:
    0 <= s.length <= 5 * 104
    s consists of English letters, digits, symbols and spaces.
"""

def lengthofLongestSubstring(s):
    l, r = 0, 0
    max_length = 0
    window = set()

    while r < len(s):
        if s[r] not in window:
            window.add(s[r])
            max_length = max(max_length, len(window))
            r += 1
        else:
            window.discard(s[l])
            l += 1

    return max_length


print(lengthofLongestSubstring("abcabcbb")) # 3
print(lengthofLongestSubstring("bbbbb")) # 1
print(lengthofLongestSubstring("pwwkew")) # 3
