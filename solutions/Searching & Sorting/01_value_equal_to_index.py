def valueEqualToIndex(arr, n):
    op = []
    for i in range(n):
        if arr[i] == i + 1:
            op.append(arr[i])
    return op

arr = [5, 2, 5, 6, 7]
print(valueEqualToIndex(arr, len(arr)))
