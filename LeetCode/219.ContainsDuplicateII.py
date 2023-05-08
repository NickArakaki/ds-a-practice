"""
Given an integer array nums and an integer k,
return true if there are two distinct indices
i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

Constraints:
    1 <= nums.length <= 105
    -109 <= nums[i] <= 109
    0 <= k <= 105
"""

# def containsNearbyDuplicate(nums, k):
#     # initialize a set
#     neighbors = set()
#     # initialize a right and left pointer to 0
#     left, right = 0, 0
#     # iterate while right pointer not out of bounds
#     while (right < len(nums)):
#         # check the window to make sure it is less than or equal to k
#         if right - left > k:
#             neighbors.remove(nums[left])
#             left += 1
#         else:
#             if nums[right] in neighbors:
#                 return True
#             else:
#                 neighbors.add(nums[right])
#                 right += 1
#     # return False
#     return False

# refactored solution
def containsNearbyDuplicate(nums, k):
    # initialize a set
    window = set()

    left = 0
    # initialize a right and left pointer to 0
    # iterate while right pointer not out of bounds
    for right in range(len(nums)):
        # first check the length of the window
        if right - left > k:
            window.remove(nums[left])
            left += 1

        if nums[right] in window:
            return True

        window.add(nums[right])
    # return False
    return False

print(containsNearbyDuplicate([1,2,3,1], 3)) # True
print(containsNearbyDuplicate([1,0,1,1], 1)) # True
print(containsNearbyDuplicate([1,2,3,1,2,3], 2)) # False
