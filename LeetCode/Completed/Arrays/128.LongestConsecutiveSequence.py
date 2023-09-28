"""
Given an unsorted array of integers nums,
return the length of the longest consecutive
elements sequence.

You must write an algorithm that runs in O(n) time.

Constraints:

    0 <= nums.length <= 105

    -109 <= nums[i] <= 109
"""

def longestConsecutive(nums):
    nums_set = set(nums)
    max_length = 0

    for num in nums_set:
        previous_num = num - 1
        next_num = num + 1
        current_length = 1

        while previous_num not in nums_set and next_num in nums_set:
            current_length += 1
            next_num += 1

        max_length = max(max_length, current_length)


    return max_length


print(longestConsecutive([100,4,200,1,3,2])) # 4
print(longestConsecutive([0,3,7,2,5,8,4,6,0,1])) # 9
