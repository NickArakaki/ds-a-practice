"""
The 26 characters of the alphabet are each assigned a security value
represented as an array of ints, where security_values[i] is
associated with the ith character of the alphabet. Given an encrypted
message, msg, and the array security_values, rearrange the characters in
msg and find the minimum possible sum of the absolute differences of the
security values of adjacent characters.
"""

def get_min_sum(security_values, msg):
    pass


print(get_min_sum([1,2,1,3,1,3,5,7,1,1,5,5,8,10,11,1,23,2,3,7,8,9,1,6,5,9], "afeb") == 2)
