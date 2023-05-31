def migratoryBirds(arr):
    buckets = [0 for i in range(5)]
    for el in arr:
        buckets[el - 1] += 1

    max_freq_el = None
    max_freq = float('-inf')
    for i, bucket in enumerate(buckets):
        if bucket > max_freq:
            max_freq_el = i + 1
            max_freq = bucket

    return max_freq_el


print(migratoryBirds([1,2,3,4,5,4,3,2,1,3,4])) # 3
# print(migratoryBirds([1,4,4,4,5,3])) # 4
