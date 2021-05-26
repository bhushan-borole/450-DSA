def row_with_max_1(arr, n, m):
    idx, curr_count = 0, arr[0].count(1)
    for i in range(1, n):
        if arr[i].count(1) > curr_count:
            idx = i
            curr_count = arr[i].count(1)
    if curr_count == 0:
        return -1
    return idx
