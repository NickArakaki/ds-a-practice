def kangaroo(x1, v1, x2, v2):
    # Write your code here
    while True:
        if x1 == x2:
            return "YES"
        elif (x1 > x2 and v1 >= v2) or (x2 > x1 and v2 >= v1):
            return "NO"

        x1 += v1
        x2 += v2

print(kangaroo(1,1,2,2)) # YES
