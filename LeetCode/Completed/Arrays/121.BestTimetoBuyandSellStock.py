"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
"""

def maxProfit(prices: list[int]) -> int:
    # keep track of potential max profit, initially 0
    max_profit = 0
    # keep track of min possible to buy at, start with inf
    min_price = float("inf")
    # iterate through list of prices
    for price in prices:
        # if current price is < current min price then reassign and continue
        if price <= min_price:
            min_price = price
        else:
            profit = price - min_price
            max_profit = max(max_profit, profit)
        # else get the difference in current price and current min price to calculate potential profit,
            # if profit > current profit reassign max profit
    # return the max profit
    return max_profit

print(maxProfit([7,1,5,3,6,4])) # 5
print(maxProfit([7,6,4,3,1])) # 0
