"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.
Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
"""

def letter_combinations(digits: str) -> list[str]:
    phone_map = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    }

    res = []

    def _backtrack(i, cur_comb):
        if len(cur_comb) == len(digits):
            res.append("".join(cur_comb))
            return

        for c in phone_map[digits[i]]:
            cur_comb.append(c)
            _backtrack(i + 1, cur_comb)
            cur_comb.pop()

    if digits:
        _backtrack(0, [])

    return res




print(letter_combinations("23") == ["ad","ae","af","bd","be","bf","cd","ce","cf"])
print(letter_combinations("") == [])
print(letter_combinations("2") == ["a", "b", "c"])
