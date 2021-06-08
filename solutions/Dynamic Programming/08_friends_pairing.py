def countFriendsPairing(n):
    dp = [0 for _ in range(n+1)]

    dp[0] = dp[1] = 1
    mod = 10**9 + 7

    for i in range(2, n+1):
        dp[i] = ((dp[i-1]) % mod + (i-1) % mod * (dp[i-2]) % mod) % mod;
    
    return dp[n]

n = 5
print(countFriendsPairing(n))
