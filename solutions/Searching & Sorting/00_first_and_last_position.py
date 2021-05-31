def find(arr, n, x):
    if x in arr:
        return arr.index(x), n - arr[::-1].index(x) - 1
    return -1, -1

arr = [1, 2, 3, 5, 5, 5, 5, 67, 99]
x = 5
print(find(arr, len(arr), x))
