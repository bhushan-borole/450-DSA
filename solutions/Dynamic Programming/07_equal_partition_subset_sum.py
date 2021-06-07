def subsetsum(arr, val):
    n = len(arr)
    dp = [[False for _ in range(val + 1)] for _ in range(n + 1)]
    
    for i in range(n + 1):
        dp[i][0] = True
    
    for i in range(1, n+1):
        for j in range(1, val+1):
            if arr[i-1] <= j:
                dp[i][j] = dp[i-1][j-arr[i-1]] or dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]
    return dp[n][val]

def equalPartition(nums):
    val = sum(nums)
    if val % 2 != 0:
        return False
    return subsetsum(nums, val//2)

arr = [1, 5, 11, 5]
print(equalPartition(arr))