"""
You are given an m x n binary matrix mat of 1's (representing soldiers) and 0's (representing civilians).
The soldiers are positioned in front of the civilians. That is, all the 1's will appear to the left of all the 0's in each row.

A row i is weaker than a row j if one of the following is true:

1) The number of soldiers in row i is less than the number of soldiers in row j.
2) Both rows have the same number of soldiers and i < j.

Return the indices of the k weakest rows in the matrix ordered from weakest to strongest.
"""

def k_weakest_rows(mat: list[list[int]], k: int) -> list[int]:
    # helper func to get num 1s in row using modified bin search
        # takes in list
        # returns int (idx of first 0)
        # init l and r pointers
        # while l < r
            # calc mid
            # if el at mid == 0 and el before mid is valid and not 0, we found the first 0
            # elif el at mid == 1 and is the last el in list, there are no 0s

    # use a dict to cache helper func results
        # key = num 1s
        # val = list of indices
    # iterate thru keys (0 -> n)
        # iterate thru list @ key
            # add el to res list until len of res == k
    # return res
    pass


print(k_weakest_rows([[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]], 3) == [2, 0, 3])

print(k_weakest_rows([[1,0,0,0],
 [1,1,1,1],
 [1,0,0,0],
 [1,0,0,0]], 2) == [0,2])
