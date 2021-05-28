def searchMatrix(matrix, target):
    for row in matrix:
        if target in row:
            return True
    return False

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [0, 1, 0, 3],
    [7, 4, 5, 6]
]
print(searchMatrix(matrix, 7))