"""
Given a string s, reverse the order of characters in each word within a sentence while still
preserving whitespace and initial word order.
"""

def reverse_words(s: str) -> str:
    # split str into words
    words = s.split(" ")
    # iterate thru words
    for i, word in enumerate(words):
        # reverse each word
        words[i] = word[::-1]
    # return reversed words joined on an empty space
    return " ".join(words)


print(reverse_words("Let's take LeetCode contest") == "s'teL ekat edoCteeL tsetnoc")
print(reverse_words("God Ding") == "doG gniD")
