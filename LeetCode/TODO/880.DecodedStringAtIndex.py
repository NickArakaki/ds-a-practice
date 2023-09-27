"""
You are given an encoded string s. To decode the string to a tape, the encoded string is read one character at a
time and the following steps are taken:

If the character read is a letter, that letter is written onto the tape.
If the character read is a digit d, the entire current tape is repeatedly written d - 1 more times in total.
Given an integer k, return the kth letter (1-indexed) in the decoded string.
"""

def decode_at_index(s: str, k: int) -> str:
    pass


print(decode_at_index("leet2code3", 10) == "o")
print(decode_at_index("ha22", 5) == "h")
print(decode_at_index("a2345678999999999999999", 1) == "a")
