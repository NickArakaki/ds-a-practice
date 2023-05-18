"""
Given an array nums with n objects colored red,
white, or blue, sort them in-place so that objects
of the same color are adjacent, with the colors
in the order red, white, and blue.

We will use the integers 0, 1, and 2 to
represent the color red, white, and blue, respectively.

You must solve this problem without using the library's
sort function.

Constraints:
    n == nums.length
    1 <= n <= 300
    nums[i] is either 0, 1, or 2.
"""

def sortColors(nums):
    buckets = [0] * 3

    for num in nums: # fill buckets
        buckets[num] += 1

    # go through buckets and replace values in order
    index = 0
    for color, value in enumerate(buckets):
        while value > 0:
            nums[index] = color
            value -= 1
            index += 1

    return nums


print(sortColors([2,0,2,1,1,0])) # [0,0,1,1,2,2]
print(sortColors([2,0,1])) # [0, 1, 2]
