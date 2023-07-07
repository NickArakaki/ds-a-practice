"""
Sherlock considers a string to be valid if all characters of the string appear the same number of times.
It is also valid if he can remove just  character at  index in the string, and the remaining characters will occur
the same number of times. Given a string , determine if it is valid. If so, return YES, otherwise return NO.
"""

def is_valid(s: str) -> str:
    # get character count in s
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1

    # create a flag to track if removed
    has_removed = False

    # iterate through char count values sorted
    sorted_count = sorted(char_count.values())
    for r in range(1, len(sorted_count)):
        prev_count = sorted_count[r - 1]
        curr_count = sorted_count[r]

        if curr_count != prev_count and not has_removed:
            sorted_count[r] -= 1
            curr_count -= 1
            has_removed = True

        if curr_count != prev_count and has_removed:
            return "NO"

    return "YES"


print(is_valid("abcdefghhgfedecba") == "YES")
print(is_valid("aabbcd") == "NO")
print(is_valid("aabbccddeefghi") == "NO")
