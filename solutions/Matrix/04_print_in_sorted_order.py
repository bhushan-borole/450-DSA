def sortedMatrix(mat, n):
    flatten = [elem for row in mat for elem in row]
    flatten.sort()
    op = [flatten[i : i+n] for i in range(0, len(flatten), n)]
    return op

matrix = [
    [10,20,30,40],
    [15,25,35,45],
    [27,29,37,48],
    [32,33,39,50]
]
print(sortedMatrix(matrix, len(matrix)))
