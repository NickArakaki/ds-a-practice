import math

"""
Koko loves to eat bananas. There are n piles of bananas,
the ith pile has piles[i] bananas. The guards have gone
and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k.
Each hour, she chooses some pile of bananas and eats k
bananas from that pile. If the pile has less than k bananas,
she eats all of them instead and will not eat any more bananas
during this hour.

Koko likes to eat slowly but still wants to finish eating
all the bananas before the guards return.

Return the minimum integer k such that she can eat
all the bananas within h hours.


Constraints:

1 <= piles.length <= 104
piles.length <= h <= 109
1 <= piles[i] <= 109
"""

def minEatingSpeed(piles: list[int], h: int) -> int:
    rates = range(1, max(piles) + 1)
    l, r = rates[0], rates[-1]
    res = r
    # binary search from 1 to largest pile
    while l <= r:
        mid = l + (r - l) // 2
        # iterate over piles list and calculate the total sum divided by rate (mid)
        total_time = 0

        for pile in piles:
            total_time += math.ceil(pile / mid)

        if total_time <= h:
            res = mid
            r = mid - 1
        elif total_time > h:
            l = mid + 1

    # if koko eats all of the bananas in h time
    return res

# print(minEatingSpeed([3,6,7,11], 8)) # 4
# print(minEatingSpeed([30,11,23,4,20], 5)) # 30
# print(minEatingSpeed([30,11,23,4,20], 6)) # 23
print(minEatingSpeed([1,1,1,999999999], 10)) # 142857143
