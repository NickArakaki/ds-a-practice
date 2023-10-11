"""
You are given a 0-indexed 2D integer array flowers, where flowers[i] = [starti, endi]
means the ith flower will be in full bloom from starti to endi (inclusive).
You are also given a 0-indexed integer array people of size n,
where people[i] is the time that the ith person will arrive to see the flowers.

Return an integer array answer of size n, where answer[i] is the number of
flowers that are in full bloom when the ith person arrives.
"""


def full_bloom_flowers(flowers: list[list[int]], people: list[int]) -> list[int]:
    # use a hash to store previously calculated vals for people and num flowers in bloom
    # init res list
    flower_count = {}
    res = []
    # iterate through people
    for person in people:
        # init count
        count = 0
        # if person not in hash
        if person not in flower_count:
            # iterate through flowers
            for start, end in flowers:
                # check person in range of flower and increment count
                if start <= person <= end:
                    count += 1
            flower_count[person] = count
        count = flower_count[person]
        res.append(count)
    return res


print(full_bloom_flowers([[1,6],[3,7],[9,12],[4,13]], [2,3,7,11]) == [1,2,2,2])
print(full_bloom_flowers([[1,10],[3,3]], [3,3,2]) == [2,2,1])
