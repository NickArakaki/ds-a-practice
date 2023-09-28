"""
Given an integer array nums and an integer k,
return the k most frequent elements.
You may return the answer in any order.

Constraints:
    1 <= nums.length <= 105

    -104 <= nums[i] <= 104

    k is in the range [1, the number of unique elements in the array].

    It is guaranteed that the answer is unique.
"""

# def topKFrequent(nums, k):
#     freq_map = {}

#     for num in nums:
#         freq_map[num] = freq_map.get(num, 0) + 1

#     freq_list = [set() for i in range(len(nums))]

#     for num, freq in freq_map.items():
#         freq_list[freq - 1].add(num)

#     res = []
#     for i in range(len(freq_list) - 1, -1, -1):
#         values = freq_list[i]
#         while len(res) < k and len(values):
#             res.append(values.pop())

#     return res


def topKFrequent(nums, k):
    freq_map = {}
    freq_list = [[] for i in range(len(nums) + 1)]

    for num in nums:
        freq_map[num] = 1 + freq_map.get(num, 0)

    for num, count in freq_map.items():
        freq_list[count].append(num)

    res = []
    for i in range(len(freq_list) - 1, 0, -1):
        for num in freq_list[i]:
            res.append(num)
            if len(res) == k:
                return res


print(topKFrequent([1,1,1,2,2,3], 2)) # [1, 2]
print(topKFrequent([1], 1)) # [1]
