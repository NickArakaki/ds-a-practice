def migratoryBirds(arr):
    arr.sort()
    curr_count = 1
    max_count = float("-inf")
    min_el = None

    for i in range(1, len(arr)):
        if arr[i - 1] == arr[i]:
            curr_count += 1
        else:
            if curr_count > max_count:
                min_el = arr[i - 1]
                max_count = curr_count
            curr_count = 1

    return min_el


print(migratoryBirds([1,2,3,4,5,4,3,2,1,3,4])) # 3
# print(migratoryBirds([1,4,4,4,5,3])) # 4
