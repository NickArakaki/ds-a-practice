"""
You are given two strings s and t.

String t is generated by random shuffling string s and then add one more letter at a random position.

Return the letter that was added to t.
"""
from collections import Counter


def find_the_difference(s: str, t: str) -> str:
    # create hash map of char frequency in s
    s_freq = Counter(s)
    # iterate through chars in t
    for char in t:
        # if char not in frequency map or val is zero, return curr char
        if (char not in s_freq) or (s_freq[char] == 0):
            return char
        # decrement char frequency
        s_freq[char] -= 1


print(find_the_difference("abcd", "abcde") == "e")
print(find_the_difference("abcd", "abcdd") == "d")
print(find_the_difference("", "y") == "y")
