"""
You are given an encoded string s. To decode the string to a tape, the encoded string is read one character at a
time and the following steps are taken:

If the character read is a letter, that letter is written onto the tape.
If the character read is a digit d, the entire current tape is repeatedly written d - 1 more times in total.
Given an integer k, return the kth letter (1-indexed) in the decoded string.
"""

# def decode_at_index(s: str, k: int) -> str:
#     # calculate total length of decoded str, up to length k
#     length = 0
#     i = 0
#     # for char in s
#     while length < k:
#         # if char is digit, multiply length by digit
#         if s[i].isdigit():
#             length *= int(s[i])
#         # else increment length
#         else:
#             length += 1
#         i += 1

#     # iterate over str in reverse order
#     for j in range(i-1, -1, -1):
#         char = s[j]
#         # if char is a digit
#         if char.isdigit():
#             # length get updated by dividing length by that digit, this removes duplicates of decoded string
#             length //= int(char)
#             # k gets updated to the modulus of k and length, only look in first copy of decoded string
#             k %= length
#         # else
#         else:
#             # if k is 0 or k == length, return the char
#             if k == 0 or k == length:
#                 return char
#             # decrement length
#             length -= 1
#     # return empty string if input is empty
#     return ""

def decode_at_index(s: str, k: int) -> str:
    # calculate total len of decoded str
    length = 0
    for char in s:
        if char.isdigit():
            length *= int(char)
        else:
            length += 1
    # iterate thru s in reverse
    for i in range(len(s) - 1, -1, -1):
        cur_char = s[i]
        # if char is digit
        if cur_char.isdigit():
            # int divide length
            length //= int(cur_char)
            # update k by mod new length, points to char in og str (ie before mult by cur digit)
            k %= length
        # else
        else:
            # if k == 0 or k == length, return char
            if k == 0 or k == length: return cur_char
            # decrement lenght
            length -= 1
    # return empty str
    return ""


# print(decode_at_index("leet2code3", 10) == "o")
"""
    "leet2code3"
    output = "o"
    k = 10

    1  2  3  4  5  6  7  8  9  10* 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36
    |  |  |  |  |  |  |  |  |  |   |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
    l  e  e  t  l  e  e  t  c  o   d  e  l  e  e  t  l  e  e  t  c  o  d  e  l  e  e  t  l  e  e  t  c  o  d  e

    length = 0
    calculate length of decoded str
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

            *
    "leet2code3"
    length = 11

             *
    "leet2code3"
    length = 12

              *
    "leet2code3"
    length = 36

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
    length = 36 // 3 = 12
    k = 10 % 12 = 10

    1  2  3  4  5  6  7  8  9  10* 11 12
    |  |  |  |  |  |  |  |  |  |   |  |
    l  e  e  t  l  e  e  t  c  o   d  e

      *
    "3edoc2teel"
    char = "e"
    length = 12 - 1 = 11
    k = 10

    1  2  3  4  5  6  7  8  9  10* 11 12
    |  |  |  |  |  |  |  |  |  |   |  |
    l  e  e  t  l  e  e  t  c  o   d  e

       *
    "3edoc2teel"
    char = "d"
    length = 11 - 1 = 10
    k = 10

    1  2  3  4  5  6  7  8  9  10* 11 12
    |  |  |  |  |  |  |  |  |  |   |  |
    l  e  e  t  l  e  e  t  c  o   d  e

        *
    "3edoc2teel"
    char = "0"
    length = 10
    k = 10
    return "o"
"""

print(decode_at_index("ha22", 5) == "h")
"""
    length = 0

    *
    "ha22"
    length = 1

    *
    "ha22"
    length = 2

    *
    "ha22"
    length = 4

        *
    "ha22"
    length = 8

    1 2 3 4 5* 6 7 8
    | | | | |  | | |
    h a h a h  a h a

     *
    "22ah"
    length = 8 // 2 = 4
    k = 5 % 4 = 1
    1* 2 3 4
    |  | | |
    h  a h a

      *
    "22ah"
    length = 4 // 2 = 2
    k = 1 % 2 = 1
    1* 2
    |  |
    h  a

       *
    "22ah"
    length = 2 - 1 = 1
    k = 1
    1* 2
    |  |
    h  a

        *
    "22ah"
    length = 1
    k = 1
    1* 2
    |  |
    h  a
    return "h"
"""
# print(decode_at_index("a2345678999999999999999", 1) == "a")
