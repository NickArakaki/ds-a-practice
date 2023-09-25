"""
We stack glasses in a pyramid, where the first row has 1 glass, the second row has 2 glasses, and so on until the 100th row.
Each glass holds one cup of champagne.

Then, some champagne is poured into the first glass at the top.
When the topmost glass is full, any excess liquid poured will fall equally to the glass immediately to the left and right of it.
When those glasses become full, any excess champagne will fall equally to the left and right of those glasses, and so on.
(A glass at the bottom row has its excess champagne fall on the floor.)

For example, after one cup of champagne is poured, the top most glass is full.
After two cups of champagne are poured, the two glasses on the second row are half full.
After three cups of champagne are poured, those two cups become full - there are 3 full glasses total now.
After four cups of champagne are poured, the third row has the middle glass half full,
and the two outside glasses are a quarter full.

Now after pouring some non-negative integer cups of champagne,
return how full the jth glass in the ith row is (both i and j are 0-indexed.)
"""


def champage_tower(poured: int, query_row: int, query_glass: int) -> float:
    pass


print(champage_tower(1, 1, 1) == 0.0000)
print(champage_tower(2, 1, 1) == 0.5000)
print(champage_tower(1000000009, 33, 17) == 1.0000)
