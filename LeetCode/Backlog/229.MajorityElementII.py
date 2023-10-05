"""
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.
"""

def majority_element(nums: list[int]) -> list[int]:
    # Boyer Moore Majority Voting Algorithm
    # init counter and tracker for 2 nums, (there can only be at most 2 el that occur more than n/3 times in any array of any len)
    # iterate thru nums
        # if num == num1:
            # increment num_1 counter
        # elif num == num2
            # increment num_2 counter
        # elif num1 counter == 0:
            # num1 = num
        # elif num2 counter == 0:
            # num2 = num
        # else
            # decrement num1 counter and num2 counter

    # set num1 counter and num2 counter to 0
    # second pass through nums to count num1 and num2
        # if num == num1:
            # increment num1 counter
        # elif num == num2:
            # increment num2 counter

    # init res list
    # if num1 counter == n // 3:
        # add num1 to res
    # if num2 counter == n // 3:
        # add num2 to res

    # return res
    pass


print(majority_element([3,2,3]) == [3])
print(majority_element([1]) == [1])
print(majority_element([1,2]) == [1,2])
