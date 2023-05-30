def marsExploration(s):
    # Write your code here
    message = "SOS"
    differences = 0

    for i, char in enumerate(s):
        mod = i % 3
        if message[mod] != char:
            differences += 1

    return differences

print(marsExploration("SOSTOT")) # 2
