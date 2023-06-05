def dynamicArray(n, queries):
    # Write your code here
    arrays = [[] for i in range(n)]
    answers = []
    lastAnswer = 0
    for query in queries:
        type, x, y = query.split(" ")
        index = (int(x) ^ lastAnswer) % n

        if type == "1":
            arrays[index].append(int(y))
        else:
            lastAnswer = arrays[index][int(y) % len(arrays[index])]
            answers.append(lastAnswer)

    return answers


print(dynamicArray(2, ["1 0 5", "1 1 7", "1 0 3", "2 1 0", "2 1 1"])) # [7, 3]
