"""
You have a long flowerbed in which some of the plots are planted, and some are not. However,
flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty,
and an integer n, return true if n new flowers can be planted in the flowerbed without violating
the no-adjacent-flowers rule and false otherwise.
"""

def can_place_flowers(flowerbed: list[int], n: int) -> bool:
    # iterate over flowerbed
    i = 0
    while n > 0 and i < len(flowerbed):
        if flowerbed[i] == 0:
            if len(flowerbed) == 1 or (i == 0 and flowerbed[i + 1] == 0) or (i == len(flowerbed) - 1 and flowerbed[i - 1] == 0) or (flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0):
                flowerbed[i] = 1
                n -= 1
        i += 1

    return True if n <= 0 else False


print(can_place_flowers([1,0,0,0,1], 1) == True)
print(can_place_flowers([1,0,0,0,1], 2) == False)
print(can_place_flowers([0,0,1,0,1], 1) == True)
print(can_place_flowers([1,0,1,0,0], 1) == True)
print(can_place_flowers([0], 1) == True)
print(can_place_flowers([0], 2) == False)
