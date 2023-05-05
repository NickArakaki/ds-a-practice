"""
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals,
and return an array of the non-overlapping intervals that cover all the intervals in the input.
"""

def merge(intervals):
    # initialize a results list
    overlapping_intervals = []
    # sort the intervals array if necessary
    intervals.sort(key = lambda sub_arr: sub_arr[0])
    # initialize a min tracker
    current_min = intervals[0][0]
    # initialize a max tracker
    current_max = intervals[0][1]

    # iterate through intervals while pointer is < intervals length
    for index in range(1, len(intervals)):
        current_interval = intervals[index]
        # if current interval min is less than or equal to the current max
        if current_interval[0] <= current_max:
            # assign min the minimum between current min and current interval min
            current_min = min(current_min, current_interval[0])
            # assign max the max between current max and current interval max
            current_max = max(current_max, current_interval[1])
        # if current interval min is greater than current max
        else:
            # push [current min, current max] to results list
            overlapping_intervals.append([current_min, current_max])
            # assign current min to current interval min
            current_min = current_interval[0]
            # assign current max to current interval max
            current_max = current_interval[1]

    # push [current min, current max] to resuts list
    overlapping_intervals.append([current_min, current_max])

    # return results list
    return overlapping_intervals

print(merge([[1,3],[2,6],[8,10],[15,18]])) # [[1,6],[8,10],[15,18]]
print(merge([[1,4],[4,5]])) # [[1,5]]
print(merge([[1,4],[0,4]])) # [[0,4]]
print(merge([[1,4],[2,3]])) # [[1,4]]
