"""
Given an integer columnNumber, return its corresponding
column title as it appears in an Excel sheet.
"""

def convert_to_tile(columnNumber: int) -> str:
    res = []

    while columnNumber > 0:
        remainder = (columnNumber - 1) % 26
        res.append(chr(ord("A") + remainder))
        columnNumber = (columnNumber - 1) // 26

    return "".join(res[::-1])

print(convert_to_tile(1) == "A")
print(convert_to_tile(28) == "AB")
print(convert_to_tile(701) == "ZY")
