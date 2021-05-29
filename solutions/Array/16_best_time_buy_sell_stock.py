def maxProfit(prices):
    if len(prices) < 2:
        return 0
    profit = 0
    curr_min = prices[0]
    
    for i in range(1, len(prices)):
        profit = max(profit, prices[i] - curr_min)
        curr_min = min(curr_min, prices[i])
    return profit

prices = [7, 1, 3, 4, 6, 2]
print(maxProfit(prices))