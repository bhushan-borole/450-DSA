def rearrange(arr, n):
    j = 0
    for i in range(n):
        if arr[i] < 0:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1
    return arr

arr = [-2, 3, 4, -5]
print(rearrange(arr, len(arr)))
