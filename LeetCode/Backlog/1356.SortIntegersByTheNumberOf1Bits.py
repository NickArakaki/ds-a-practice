"""
You are given an integer array arr.
Sort the integers in the array in ascending order by the number of 1's in
their binary representation and in case of two or more integers have the
same number of 1's you have to sort them in ascending order.

Return the array after sorting it.
"""
import heapq

def sort_by_bits(arr: list[int]) -> list[int]:
    dp = [[] for _ in range(32)]
    for num in arr:
        count = 0
        for char in bin(num):
            if char == "1":
                count += 1
        heapq.heappush(dp[count], num)

    res = []
    for heap in dp:
        while heap:
            res.append(heapq.heappop(heap))

    return res

print(sort_by_bits([0,1,2,3,4,5,6,7,8]) == [0,1,2,4,8,3,5,6,7])
print(sort_by_bits([1024,512,256,128,64,32,16,8,4,2,1]) == [1,2,4,8,16,32,64,128,256,512,1024])
