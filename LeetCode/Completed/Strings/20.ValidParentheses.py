"""
Given a string s containing just the characters '(', ')', '{', '}',
'[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
"""

def isValid(s: str) -> bool:
    stack = []
    parentheses_map = {
                        "}" : "{",
                        ")": "(",
                        "]": "["
                    }

    for char in s:
        if char in parentheses_map:
            if len(stack):
                compliment = stack.pop()
                if compliment != parentheses_map[char]:
                    return False
            else:
                return False
        else:
            stack.append(char)

    return True if len(stack) == 0 else False

print(isValid("()")) # true
print(isValid("()[]{}")) # true
print(isValid("(]")) # false
