def maxSubArraySum(arr, n):
    max_so_far = float('-inf')
    max_ending_here = 0

    for elem in arr:
        max_ending_here += elem
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
        if max_ending_here < 0:
            max_ending_here = 0
    return max_so_far


arr = [1, 2, 3, -2, 5]
print(maxSubArraySum(arr, len(arr)))
