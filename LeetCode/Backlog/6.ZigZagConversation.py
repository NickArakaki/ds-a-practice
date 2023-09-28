"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given
number of rows like this: (you may want to display this pattern in a
fixed font for better legibility)

P (0)       A (4)        H (8)         N (12)
A (1) P (3) L (5) S (7)  I (9)  I (11) G (13)
Y (2)       I (6)        R (10)

output: "PAHNAPLSIIGYIR"
"""

def convert(s: str, num_rows: int) -> str:
    char_lists = [[] for _ in range(num_rows)]
    offset = 0

    for idx, char in enumerate(s):
        pass





print(convert("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR")
print(convert("PAYPALISHIRING", 4) == "PINALSIGYAHRPI")
print(convert("A", 1) == "A")
