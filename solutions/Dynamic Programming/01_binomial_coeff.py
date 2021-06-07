def nCr(n, r):
    dp = [[0 for _ in range(r+1)] for _ in range(n+1)]
        
    for i in range(n+1):
        dp[i][0] = 1
    
    for i in range(1, n+1):
        for j in range(1, r+1):
            if i == j:
                dp[i][j] = 1
            if i < j:
                dp[i][j] = 0
            else:
                dp[i][j] = (dp[i-1][j] + dp[i-1][j-1]) % 1000000007
    return dp[n][r]

n = 5
r = 3
print(nCr(n, r))