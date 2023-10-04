"""
An analyst is analyzing a stock over a period of n days. The price of the stock on the ith day is price[i],
and the profit obtained is denoted by profit[i]. The analyst wants to pick a triplet of days (i,j,k) such that
(i < j < k) adn price[i] < price[j] < price[k] in such a way that the total profit, i.e. profit[i] + profit[j] + profit[k]
is maximized.
Find the maximum total profit possible, if there is no valid triplet, return -1
"""

def max_profit(price, profit):
    # map profits to days
    profit_map = {} # potential edge case if multiple days have the same profit val, maybe store as a set?
    for day, val in enumerate(profit):
        profit_map[val] = day
    # sort profits
    profit.sort()
    # track cur sum
    cur_sum = 0
    max_sum = -1
    l = 0
    for r in range(len(profit)):
        window = r - l + 1
        while window > 3:
            cur_sum -= profit[l]
            l += 1
        cur_sum += profit[r]
        if window == 3 and price[profit_map[profit[l]]] < price[profit_map[profit[l + 1]]] < price[profit_map[profit[r]]]:
            max_sum = max(max_sum, cur_sum)

    return max_sum


print(max_profit([1,5,3,4,6], [2,3,4,5,6]) == 15)
