def diagonalDifference(arr):
    primary_diagonal_sum = secondary_diagonal_sum = 0

    for i in range(len(arr)):
        primary_value = arr[i][i]
        secondary_value = arr[i][(len(arr) - i - 1)]
        primary_diagonal_sum += primary_value
        secondary_diagonal_sum += secondary_value

    return abs(secondary_diagonal_sum - primary_diagonal_sum)

print(diagonalDifference([[1,2,3], [4,5,6], [9,8,9]])) # 2
