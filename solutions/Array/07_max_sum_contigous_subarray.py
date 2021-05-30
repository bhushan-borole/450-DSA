# Using normal DP
# We can also solve this using Kadane Algorithm
# Check here: https://github.com/bhushan-borole/450-DSA/blob/master/solutions/Array/12_kadane.py
def maxSubArraySum(arr, n):
    dp = [0] * (n + 1)
    for i in range(n-1, -1, -1):
        dp[i] = arr[i] + max(dp[i+1], 0)
    return max(dp)

arr = [1, 2, 3, -2, 5]
print(maxSubArraySum(arr, len(arr)))
