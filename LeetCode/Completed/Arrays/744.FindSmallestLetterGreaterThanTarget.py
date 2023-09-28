"""
You are given an array of characters letters that is
sorted in non-decreasing order, and a character target.
There are at least two different characters in letters
Return the smallest character in letters that is lexicographically
greater than target. If such a character does not exist, retun the
first character in letters.
"""

def nextGreatestLetter(letters: list[str], target: str) -> str:
    l, r = 0, len(letters) - 1

    if letters[-1] <= target:
        return letters[0]

    ans = None

    while l <= r:
        mid = (l + r) // 2
        letter = letters[mid]
        if target < letter: # search left
            ans = letter
            r = mid - 1
        else: # search right
            l = mid + 1

    return ans



print(nextGreatestLetter(["c","f","j"], "a")) # "c"
print(nextGreatestLetter(["c","f","j"], "c")) # "f"
print(nextGreatestLetter(["x","x","y","y"], "z")) # "x"
