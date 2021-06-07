def nPk(n, k):
    dp = [[0 for _ in range(k+1)] for _ in range(n+1)]

    for i in range(n+1):
        dp[i][0] = 1
    
    for i in range(1, n+1):
        for j in range(1, k+1):
            if i == j:
                dp[i][j] = 1
            if i < j:
                dp[i][j] = 0
            else:
                dp[i][j] = dp[i-1][j] + (j * dp[i-1][j-1])
    return dp[n][k]

n = 10
k = 8
print(nPk(n, k))