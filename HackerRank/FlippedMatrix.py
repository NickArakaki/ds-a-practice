def flippedMatrix(matrix):
    max_sum = 0

    for i in range((len(matrix) // 2)):
        i_compliment = len(matrix) - 1 - i

        for j in range((len(matrix) // 2)):
            j_compliment = len(matrix) - 1 - j

            val_1 = matrix[i][j]
            val_2 = matrix[i][j_compliment]
            val_3 = matrix[i_compliment][j]
            val_4 = matrix[i_compliment][j_compliment]
            max_sum += max(val_1, val_2, val_3, val_4)

    return max_sum

print(flippedMatrix([[1,2,3, 5], [3,4, 5, 6], [4, 5, 6, 7], [8,9,10, 11]]))
