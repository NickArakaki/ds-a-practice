"""
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?
"""

import heapq

def find_kth_largest(nums: list[int], k: int) -> int:
    # heapify nums
    heap = nums[:k]
    heapq.heapify(heap)

    for num in nums[k:]:
        print(num)
        if num > heap[0]:
            heapq.heappop(heap)
            heapq.heappush(heap, num)

    return heap[0]


# def find_kth_largest(nums: list[int], k: int) -> int:
#     nums.sort()
#     return nums[-k]


# print(find_kth_largest([3,2,1,5,6,4], 2) == 5)
# print(find_kth_largest([3,2,3,1,2,4,5,5,6], 4) == 4)
# print(find_kth_largest([2,1], 2) == 1)
print(find_kth_largest([-1,2,0], 2) == 0)
# print(find_kth_largest([1], 1) == 1)
