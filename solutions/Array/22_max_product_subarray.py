def maxProduct(arr):
    op = arr[0]
    curr_max = curr_min = op
    for elem in arr[1:]:
        if elem < 0:
            curr_max, curr_min = curr_min, curr_max
        curr_max = max(curr_max * elem, elem)
        curr_min = min(curr_min * elem, elem)
        op = max(op, curr_max)
    return op

arr = [2,3,-2,4]
print(maxProduct(arr))
