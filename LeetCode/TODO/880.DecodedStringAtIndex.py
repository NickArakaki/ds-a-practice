"""
You are given an encoded string s. To decode the string to a tape, the encoded string is read one character at a
time and the following steps are taken:

If the character read is a letter, that letter is written onto the tape.
If the character read is a digit d, the entire current tape is repeatedly written d - 1 more times in total.
Given an integer k, return the kth letter (1-indexed) in the decoded string.
"""

def decode_at_index(s: str, k: int) -> str:
    # calculate total length of decoded str, up to length k
    length = 0
    i = 0
    # for char in s
    while length < k:
        # if char is digit, multiply length by digit
        if s[i].isdigit():
            length *= int(s[i])
        # else increment length
        else:
            length += 1
        i += 1

    # iterate over str in reverse order
    for j in range(i-1, -1, -1):
        char = s[j]
        # if char is a digit
        if char.isdigit():
            # length get updated by dividing length by that digit
            length //= int(char)
            # k gets updated to the modulus of k and length
            k %= length
        # else
        else:
            # if k is 0 or k == length, return the char
            if k == 0 or k == length:
                return char
            # decrement length
            length -= 1
    # return empty string if input is empty
    return ""


print(decode_at_index("leet2code3", 10) == "o")
print(decode_at_index("ha22", 5) == "h")
print(decode_at_index("a2345678999999999999999", 1) == "a")
