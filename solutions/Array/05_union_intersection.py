def union(arr1, arr2):
    return len(set(arr1 + arr2))

def intersection(arr1, arr2):
    return len(set(arr1).intersection(set(arr2)))

arr1 = [1, 1, 2, 3, 3, 4, 5]
arr2 = [5, 6, 7]

print(union(arr1, arr2))
print(intersection(arr1, arr2))
