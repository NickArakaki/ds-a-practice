def gamingArray(arr):

    def _map_array(array):
        array_map = {}
        curr_max = float('-inf')
        curr_max_index = None

        for idx, el in enumerate(array):
            if el > curr_max:
                curr_max = el
                curr_max_index = idx
            array_map[idx] = curr_max_index

        return array_map

    arr_map = _map_array(arr)
    turn = 0

    i = len(arr) - 1
    while i >= 0:
        max_idx = arr_map[i]
        i = max_idx - 1
        turn += 1

    return "BOB" if turn % 2 == 1 else "ANDY"


print(gamingArray([2,3,5,4,1])) # BOB
