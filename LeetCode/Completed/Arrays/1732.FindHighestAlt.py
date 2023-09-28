"""
There is a biker going on a road trip. The road trip consists of n + 1
points at different altitudes. The biker starts his trip on point 0 with altitude equal 0.

You are given an integer array gain of length n where gain[i] is the net
gain in altitude between points i​​​​​​ and i + 1 for all (0 <= i < n). Return the highest altitude of a point.
"""

def largestAltitude(gain: list[int]) -> int:
    curr_alt = max_alt = 0
    for alt in gain:
        curr_alt += alt
        max_alt = max(curr_alt, max_alt)
    return max_alt

print(largestAltitude([-5,1,5,0,-7])) # 1
print(largestAltitude([-4,-3,-2,-1,4,3,2])) # 0
