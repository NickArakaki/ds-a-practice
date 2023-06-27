"""
You are given two integer arrays nums1 and nums2 sorted in ascending order and an integer k.

Define a pair (u, v) which consists of one element from the first array and one element from the second array.

Return the k pairs (u1, v1), (u2, v2), ..., (uk, vk) with the smallest sums.
"""

def kSmallestPairs(nums1: list[int], nums2:list[int], k: int) -> list[list[int]]:
    res = []
    # initialize idx1, idx2 to 0
    idx1, idx2 = 0, 0
    # iterate through both nums1 and nums2 while res list length < k and less than all possible pairs(n * m)
    while len(res) < k and len(res) < (len(nums1) * len(nums2)):
        # add values at nums1[idx1], nums2[idx2] to res list
        res.append([nums1[idx1], nums2[idx2]])
        # if at the end of one list increment the other
        if (idx1 < len(nums1) - 1) and (idx2 < len(nums2) - 1) :
            num1_next = nums1[idx1 + 1]
            num2_next = nums2[idx2 + 1]
            if num1_next < num2_next:
                idx1 += 1
            else:
                idx2 += 1
        elif (idx2 < len(nums2) - 1):
            idx2 += 1
        elif (idx1 < len(nums1) - 1):
            idx1 += 1

    # return res list
    return res

# print(kSmallestPairs([1,7,11], [2,4,6], 3)) # [[1,2],[1,4],[1,6]]
print(kSmallestPairs([1,1,2], [1,2,3], 10)) # [[1,1],[1,1],[2,1],[1,2],[1,2],[2,2],[1,3],[1,3],[2,3]]
# print(kSmallestPairs([1,1,2], [1,2,3], 2)) # [[1,1],[1,1]]
# print(kSmallestPairs([1,2], [3], 3)) # [[1,3],[2,3]]
