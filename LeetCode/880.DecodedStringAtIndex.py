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
"""
    "leet2code3"
    output = "o"
    k = 10

    1  2  3  4  5  6  7  8  9  10* 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36
    |  |  |  |  |  |  |  |  |  |   |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
    l  e  e  t  l  e  e  t  c  o   d  e  l  e  e  t  l  e  e  t  c  o  d  e  l  e  e  t  l  e  e  t  c  o  d  e

    length = 0
    calculate where to start by getting length up to or just beyond k (while length < k)
    if char is a digit multiply current length by digit
    else increment length

     *
    "leet2code3"
    length = 1

      *
    "leet2code3"
    length = 2

       *
    "leet2code3"
    length = 3

        *
    "leet2code3"
    length = 4

         *
    "leet2code3"
    length = 8

          *
    "leet2code3"
    length = 9

           *
    "leet2code3"
    length = 10

    iterate in reverse
    if char is a digit, length //= digit, k %= length
    else if k == 0 or k == length, return char
    else decrement length

    1  2  3  4  5  6  7  8  9  10* 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36
    |  |  |  |  |  |  |  |  |  |   |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
    l  e  e  t  l  e  e  t  c  o   d  e  l  e  e  t  l  e  e  t  c  o  d  e  l  e  e  t  l  e  e  t  c  o  d  e

     *
    "3edoc2teel"
    char = "3"
    length = 10 // 3 = 3
    k = 10 % 3 = 1

      *
    "3edoc2teel"
    char = "e"
    length = 3 - 1 = 2
    k = 1

       *
    "3edoc2teel"
    char = "d"
    length = 2 - 1 = 1
    k = 1

        *
    "3edoc2teel"
    char = "o"
    length = 1
    k = 1
    return "o"
"""

# print(decode_at_index("ha22", 5) == "h")
# print(decode_at_index("a2345678999999999999999", 1) == "a")
