"""
You have a long flowerbed in which some of the plots are planted, and some are not. However,
flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty,
and an integer n, return true if n new flowers can be planted in the flowerbed without violating
the no-adjacent-flowers rule and false otherwise.
"""

def can_place_flowers(flowerbed: list[int], n: int) -> bool:
    pass


print(can_place_flowers([1,0,0,0,1], 1) == True)
print(can_place_flowers([1,0,0,0,1], 2) == False)
print(can_place_flowers([0,0,1,0,1], 1) == True)
