"""
You are given the customer visit log of a shop represented by a 0-indexed string customers consisting only of characters 'N' and 'Y':

if the ith character is 'Y', it means that customers come at the ith hour
whereas 'N' indicates that no customers come at the ith hour.
If the shop closes at the jth hour (0 <= j <= n), the penalty is calculated as follows:

For every hour when the shop is open and no customers come, the penalty increases by 1.
For every hour when the shop is closed and customers come, the penalty increases by 1.
Return the earliest hour at which the shop must be closed to incur a minimum penalty.

Note that if a shop closes at the jth hour, it means the shop is closed at the hour j.

1 <= customers.length <= 10^5
customers consists only of characters "Y" and "N"
"""

def best_closing_time(customers: str) -> int:
    # track current penalty
    # track min penalty
    curr_pen = min_pen = 0
    # track min closing time
    min_close = len(customers)

    # iterate through customers (get penalty for closing time at len(customers))
        # if no customers increment penalty
    for customer in customers:
        if customer == "N":
            min_pen += 1
            curr_pen += 1

    # iterate through customers in reverse
    for hour in range(len(customers) - 1, -1, -1):
        customer = customers[hour]
        # if there are customers increment penalty
        if customer == "Y":
            curr_pen += 1
        # else decrement penalty
        else:
            curr_pen -= 1
        # if curr penalty <= min penalty
        if curr_pen <= min_pen:
            # reassign min penalty to curr penalty
            min_pen = curr_pen
            # reassign min closing time to curr index
            min_close = hour

    # return min closing time
    return min_close


print(best_closing_time("YYNY")) # 2
print(best_closing_time("NNNNN")) # 0
print(best_closing_time("YYYY")) # 4
