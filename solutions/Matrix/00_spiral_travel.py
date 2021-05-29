def traverse(matrix):
    a = []
    while len(matrix)>0:
        a += list(matrix[0])
        matrix = matrix[1:][:]
        # transpose
        matrix = list(map(list, zip(*matrix)))
        # reverse the matrix (reversing the rows)
        matrix = matrix[::-1]
    return a

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]
print(traverse(matrix))
