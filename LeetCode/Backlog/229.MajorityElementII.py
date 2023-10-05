"""
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.
"""

def majority_element(nums: list[int]) -> list[int]:
    # Boyer Moore Majority Voting Algorithm
    # init counter and tracker for 2 nums, (there can only be at most 2 el that occur more than n/3 times in any array of any len)
    num_1, num_2, counter_1, counter_2 = 0, 0, 0, 0

    for num in nums:
        if num == num_1:
            counter_1 += 1
        elif num == num_2:
            counter_2 += 1
        elif counter_1 == 0:
            num_1 = num
            counter_1 += 1
        elif counter_2 == 0:
            num_2 = num
            counter_2 += 1
        else:
            counter_1 -= 1
            counter_2 -= 1

    # set num1 counter and num2 counter to 0
    counter_1 = counter_2 = 0
    for num in nums:
        if num == num_1:
            counter_1 += 1
        elif num == num_2:
            counter_2 += 1

    res = []
    n = len(nums)
    if counter_1 > (n / 3):
        res.append(num_1)
    if counter_2 > (n / 3):
        res.append(num_2)

    return res

print(majority_element([3,2,3]) == [3])
print(majority_element([1]) == [1])
print(majority_element([1,2]) == [1,2])
