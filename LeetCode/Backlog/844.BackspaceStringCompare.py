"""
Given two strings s and t, return true if they are equal when both are typed into empty text editors.
'#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.
"""

def backspace_compare(s: str, t: str) -> bool:
    pass


print(backspace_compare("ab#c", "ad#c") == True)
print(backspace_compare("ab##", "c#d#") == True)
print(backspace_compare("a#c", "b") == False)
print(backspace_compare("", "#########") == True)
