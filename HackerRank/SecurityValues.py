"""
The 26 characters of the alphabet are each assigned a security value
represented as an array of ints, where security_values[i] is
associated with the ith character of the alphabet. Given an encrypted
message, msg, and the array security_values, rearrange the characters in
msg and find the minimum possible sum of the absolute differences of the
security values of adjacent characters.
"""
from heapq import heappush, heappop

# def get_min_sum(security_values, msg):
#     values = []
#     for char in msg:
#         index = ord(char.lower()) - ord("a")
#         values.append(security_values[index])
#     # sort list
#     values.sort()
#     diff_sum = 0
#     # iterate through list and get absolute val of each el and neighbor, add to sum
#     for i, val in enumerate(values[:-1:]):
#         diff_sum += abs(val - values[i + 1])
#     # return sum
#     return diff_sum


def get_min_sum(security_values, msg):
    values = []
    for char in msg:
        index = ord(char.lower()) - ord("a")
        heappush(values, security_values[index])

    diff_sum = 0
    prev = heappop(values)
    while values:
        val = heappop(values)
        diff_sum += abs(prev - val)
        prev = val

    return diff_sum


print(get_min_sum([1,2,1,3,1,3,5,7,1,1,5,5,8,10,11,1,23,2,3,7,8,9,1,6,5,9], "afeb") == 2)
