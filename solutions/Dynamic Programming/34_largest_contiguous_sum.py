def maxSubArraySum(a, size):
    dp = [0] * (size + 1)
    for i in range(size-1, -1, -1):
        dp[i] = a[i] + max(dp[i+1], 0)
    return max(dp)

arr = [1, 2, 3, -2, 5]
print(maxSubArraySum(arr, len(arr)))
