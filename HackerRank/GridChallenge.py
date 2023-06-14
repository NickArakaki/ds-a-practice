def gridChallenge(grid):
    sorted_rows = ["".join(sorted(row)) for row in grid] # O(m * nlogn)

    # iterate through columns
    for col in range(len(sorted_rows[0])):
        prev_char = sorted_rows[0][col]
        for row in range(len(sorted_rows)):
            curr_char = sorted_rows[row][col]
            if curr_char < prev_char:
                return "NO"
    return "YES"


print(gridChallenge(["abc", "ade", "efg"])) # YES
print(gridChallenge(["eabcd", "fghij", "olkmn", "trqps", "xywuv"])) # YES
print(gridChallenge(["uxf", "vof", "hmp"])) # NO
print(gridChallenge(["kc", "iu"])) # YES
