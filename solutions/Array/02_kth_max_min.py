def kth_min(arr, k):
    arr.sort()
    return arr[k-1]

def kth_max(arr, k):
    arr.sort(reverse=True)
    return arr[k-1]

arr = [7, 10, 4, 3, 20, 15]
print(kth_max(arr, 3))
print(kth_min(arr, 3))
