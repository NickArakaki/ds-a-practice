"""
An image is represented by an m x n integer grid image where image[i][j]
represents the pixel value of the image.

You are also given three integers sr, sc, and color. You should perform a
flood fill on the image starting from the pixel image[sr][sc].

To perform a flood fill, consider the starting pixel, plus any pixels connected
4-directionally to the starting pixel of the same color as the starting pixel,
plus any pixels connected 4-directionally to those pixels (also with the same color),
and so on. Replace the color of all of the aforementioned pixels with color.

Return the modified image after performing the flood fill.
"""

from collections import deque

def floodFill(image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
    # use a set to keep track of values aleady visited
    visited_pixels = set()
    queue = deque()
    start_val = image[sr][sc]
    start = (sr, sc)
    visited_pixels.add(start)
    queue.append(start)

    while queue:
        curr_row, curr_col = queue.popleft()
        curr_pixle_val = image[curr_row][curr_col]

        if curr_pixle_val == start_val:
            image[curr_row][curr_col] = color
            if curr_row - 1 >= 0:
                up = (curr_row - 1, curr_col)
                if up not in visited_pixels:
                    visited_pixels.add(up)
                    queue.append(up)
            if curr_row + 1 < len(image):
                down = (curr_row + 1, curr_col)
                if down not in visited_pixels:
                    visited_pixels.add(down)
                    queue.append(down)
            if curr_col + 1 < len(image[0]):
                right = (curr_row, curr_col + 1)
                if right not in visited_pixels:
                    visited_pixels.add(right)
                    queue.append(right)
            if curr_col - 1 >= 0:
                left = (curr_row, curr_col - 1)
                if left not in visited_pixels:
                    visited_pixels.add(left)
                    queue.append(left)
    return image

print(floodFill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2)) # [[2,2,2],[2,2,0],[2,0,1]]
