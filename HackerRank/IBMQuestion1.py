"""
An analyst is analyzing a stock over a period of n days. The price of the stock on the ith day is price[i],
and the profit obtained is denoted by profit[i]. The analyst wants to pick a triplet of days (i,j,k) such that
(i < j < k) adn price[i] < price[j] < price[k] in such a way that the total profit, i.e. profit[i] + profit[j] + profit[k]
is maximized.
Find the maximum total profit possible, if there is no valid triplet, return -1
"""

def max_profit(price, profit):
    # map profits to days
    # sort profits
    # track cur sum
    # track max sum
    # iterate through sorted profits with sliding window
        # if current window is greater than 3:
            # move left adjust left pointer until it's correct size
        # add r val to cur sum
        # if window len == 3
            # check prices with mapped profit values
    # return max sum
    pass


print(max_profit([1,5,3,4,6], [2,3,4,5,6]) == 15)
