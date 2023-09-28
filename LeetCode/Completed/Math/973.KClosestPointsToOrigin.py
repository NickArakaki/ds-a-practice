"""
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).
"""

from math import sqrt
import heapq

def kClosest(points: list[list[int]], k: int) -> list[list[int]]:
    distance_coord_list = []
    for point in points:
        x, y = point
        distance = sqrt(x**2 + y**2)
        distance_coord_list.append((distance, point))

    heapq.heapify(distance_coord_list)
    res = []
    for _ in range(k):
        distance, coord = heapq.heappop(distance_coord_list)
        res.append(coord)

    return res

print(kClosest([[1,3],[-2,2]], 1)) # [[-2, 2]]
print(kClosest([[3,3],[5,-1],[-2,4]], 2)) # [[3,3],[-2,4]]
