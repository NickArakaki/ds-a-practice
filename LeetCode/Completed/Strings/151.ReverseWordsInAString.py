"""
Given an input string s,
reverse the order of the words.

A word is defined as a sequence
of non-space characters. The words
in s will be separated by at least
one space.

Return a string of the words in
reverse order concatenated by a
single space.

Note that s may contain leading or
trailing spaces or multiple spaces
between two words. The returned
string should only have a single space
separating the words. Do not include
any extra spaces.

Constraints:

    1 <= s.length <= 104

    s contains English letters (upper-case and lower-case),
    digits, and spaces ' '.

    There is at least one word in s.

"""

def reverseWords(s: str) -> str:
    words = s.split(" ")
    reversed_words = []
    for i in range(len(words) - 1, -1, -1):
        if words[i]:
            reversed_words.append(words[i])

    return " ".join(reversed_words)

print(reverseWords("the sky is blue") == "blue is sky the") # "blue is sky the"
print(reverseWords("  hello world  ") == "world hello") # "world hello"
print(reverseWords("a good   example") == "example good a") # "example good a"
