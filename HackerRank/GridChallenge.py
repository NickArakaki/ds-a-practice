def gridChallenge(grid):
    sorted_rows = ["".join(sorted(row)) for row in grid]

print(gridChallenge(["abc", "ade", "efg"])) # YES
# print(gridChallenge(["eabcd", "fghij", "olkmn", "trqps", "xywuv"])) # YES
