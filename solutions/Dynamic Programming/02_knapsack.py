def knapsack(weights, values, W, n):
    dp = [[0 for _ in range(W+1)] for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, W+1):
            if weights[i-1] <= j:
                dp[i][j] = max(
                    values[i-1] + dp[i - 1][j-weights[i-1]],
                    dp[i-1][j]
                )
            else:
                dp[i][j] = dp[i-1][j]
    return dp[n][W]

weights = [1, 2, 3]
values = [4, 5, 1]
W = 3
n = 3
print(knapsack(weights, values, W, n))