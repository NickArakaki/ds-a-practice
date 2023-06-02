from collections import defaultdict

def closestNumber(arr: list[int]) -> list[int]:
    arr.sort()
    difference_map = defaultdict(list)
    min_diff = float('inf')

    for i in range(1, len(arr)):
        difference = arr[i] - arr[i - 1]
        difference_map[difference].extend([arr[i - 1], arr[i]])
        min_diff = min(min_diff, difference)

    return difference_map[min_diff]


print(closestNumber([5,4,3,2])) # [2,3,3,4,4,5]
print(closestNumber([-20, -3916237, -357920, -3620601, 7374819, -7330761, 30, 6246457, -6461594, 266854, -520, -470 ])) # [-520, -470, -20, 30]
