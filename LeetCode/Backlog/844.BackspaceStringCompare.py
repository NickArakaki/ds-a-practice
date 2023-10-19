"""
Given two strings s and t, return true if they are equal when both are typed into empty text editors.
'#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

Constraints:
1 <= len(s), len(t) <= 200
s and t contain only lowercase letters and "#" characters
"""

# Brute Force: build create each string, and compare at the end
def backspace_compare(s: str, t: str) -> bool:
    # new_s, new_t = "", ""
    # s_back, t_back = 0, 0
    # iterate thru each word in reverse
        # if current char == "#":
            # increment num backs
        # elif num backs > 0:
            # decrement num backs
        # else
            # add char to beginning of new str

    # return comparison of new_s to new_t

    pass


print(backspace_compare("ab#c", "ad#c") == True)
print(backspace_compare("ab##", "c#d#") == True)
print(backspace_compare("a#c", "b") == False)
print(backspace_compare("#", "#########") == True)
