"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Constraints:
    n == height.length
    2 <= n <= 105
    0 <= height[i] <= 104
"""

def maxArea(height):
    l, r = 0, len(height) - 1

    max_area = 0

    while l < r:
        smallest_height = min(height[l], height[r])
        calculated_area = smallest_height * (r - l)
        max_area = max(max_area, calculated_area)

        if height[l] < height[r]:
            l += 1
        else:
            r -= 1

    return max_area


print(maxArea([1,8,6,2,5,4,8,3,7])) # 49
print(maxArea([1, 1])) # 1
