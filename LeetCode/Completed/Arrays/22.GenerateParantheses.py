"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
"""

def generate_parenthesis(n: int) -> list[str]:
    ans = []

    def _backtrack(num_open, num_closed, combo):
        if len(combo) == 2 * n:
            ans.append("".join(combo))
            return

        # decision to add open
            # if num open < n and not the last element being added
        if num_open < n:
            combo.append("(")
            _backtrack(num_open + 1, num_closed, combo)
            combo.pop()

        # decision to add closed
            # only if num open > num closed and num closed < n
        if num_open > num_closed:
            combo.append(")")
            _backtrack(num_open, num_closed + 1, combo)
            combo.pop()

    _backtrack(1, 0, ["("])

    return ans

print(generate_parenthesis(3)) # ["((()))","(()())","(())()","()(())","()()()"]
print(generate_parenthesis(1)) # ["()"]
