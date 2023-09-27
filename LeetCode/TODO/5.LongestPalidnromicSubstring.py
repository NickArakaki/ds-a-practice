"""
Given a string s, return the longest
palindromic substring in s.

Trick is to check if palindrome inside-out rather that outside-in and account for even and odd len strs
"""

def longest_palindrom(s: str) -> str:
    # init res str
    # iterate through each char of s
        # first check for odd len palindrome
        # init l and r pointers to be same position
        # while l and r pointers are inbound and the val at l and r are equal
            # move pointers outward
            # if current len substring > max substring, update

        # check if even len palindrom
        # r points to next char in str
        # while l and r are inbounds and chars at l and r are equal
            # move pointers
            # update accordingly
        # return res str
    pass


print(longest_palindrom("babad") == "bab")
print(longest_palindrom("cbbd") == "bb")
