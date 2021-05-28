# Method 1
def sort(arr, n):
    count_0 = arr.count(0)
    count_1 = arr.count(1)
    count_2 = arr.count(2)
    
    for i in range(count_0):
        arr[i] = 0
    
    if count_1 != 0:
        for i in range(count_0, count_0 + count_1):
            arr[i] = 1
    
    if count_2 != 0:
        for i in range(count_0 + count_1, n):
            arr[i] = 2
    return arr

# Method 2:
def sort1(arr, n):
    low, mid, high = 0, 0, n - 1
    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        elif arr[mid] == 2:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
    return arr

arr = [0, 2, 1, 2, 0]
print(sort1(arr, 5))
