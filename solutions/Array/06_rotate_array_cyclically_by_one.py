def rotate(arr, n):
    # modify the arr itself, without creating a new arr
    temp = arr[n-1]
    for i in range(n-1, -1, -1):
        arr[i] = arr[i-1]
    arr[0] = temp
    return arr

arr = [1, 2]
n = 2
print(rotate(arr, 2))