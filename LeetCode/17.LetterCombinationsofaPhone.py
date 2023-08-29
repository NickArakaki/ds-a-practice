"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.
Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
"""

def letter_combinations(digits: str) -> list[str]:
    pass


print(letter_combinations("23") == ["ad","ae","af","bd","be","bf","cd","ce","cf"])
print(letter_combinations("") == [])
print(letter_combinations("2") == ["a", "b", "c"])
