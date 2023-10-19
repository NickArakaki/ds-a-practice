"""
Given two strings s and t, return true if they are equal when both are typed into empty text editors.
'#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

Constraints:
1 <= len(s), len(t) <= 200
s and t contain only lowercase letters and "#" characters
"""

# Brute Force: build create each string, and compare at the end
# def backspace_compare(s: str, t: str) -> bool:
#     # new_s, new_t = "", ""
#     # s_back, t_back = 0, 0
#     # iterate thru each word in reverse
#         # if current char == "#":
#             # increment num backs
#         # elif num backs > 0:
#             # decrement num backs
#         # else
#             # add char to beginning of new str

#     # return comparison of new_s to new_t
#     new_s, new_t = "", ""
#     s_back, t_back = 0, 0
#     for s_i in range(len(s) - 1, -1, -1):
#         char = s[s_i]
#         if char == "#":
#             s_back += 1
#         elif s_back > 0:
#             s_back -= 1
#         else:
#             new_s = char + new_s

#     for t_i in range(len(t) - 1, -1, -1):
#         char = t[t_i]
#         if char == "#":
#             t_back += 1
#         elif t_back > 0:
#             t_back -= 1
#         else:
#             new_t = char + new_t

#     return new_s == new_t

# Stack solution
def backspace_compare(s: str, t: str) -> bool:
    # create s and t stack
    s_stack, t_stack = [], []
    for i in range(len(s)):
        if s_stack and s[i] == "#":
            s_stack.pop()
        if s[i] != "#":
            s_stack.append(s[i])

    for i in range(len(t)):
        if t_stack and t[i] == "#":
            t_stack.pop()
        if t[i] != "#":
            t_stack.append(t[i])

    return s_stack == t_stack



# print(backspace_compare("ab#c", "ad#c") == True)
# print(backspace_compare("ab##", "c#d#") == True)
# print(backspace_compare("a#c", "b") == False)
# print(backspace_compare("#", "#########") == True)
print(backspace_compare("y#fo##f", "y#f#o##f") == True)
