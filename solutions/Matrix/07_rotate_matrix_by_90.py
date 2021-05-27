def rotate(matrix):
    """
    Do not return anything, modify matrix in-place instead.
    """
    matrix.reverse()
    for i in range(len(matrix)):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i],matrix[i][j]
