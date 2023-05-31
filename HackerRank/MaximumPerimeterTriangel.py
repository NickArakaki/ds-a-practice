def maximumPerimeterTriange(sticks):
    sticks.sort()

    for i in range(len(sticks) - 1, 1, -1):
        longest = sticks[i]
        second_longest = sticks[i - 1]
        smallest = sticks[i - 2]
        if longest < (second_longest + smallest):
            return [smallest, second_longest, longest]

    return [-1]

print(maximumPerimeterTriange([1,2,3,4,5,10])) # [3,4,5]
