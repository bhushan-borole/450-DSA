import statistics

def median(mat):
    flatten = [elem for row in mat for elem in row]
    return statistics.median(flatten)

matrix = [
    [1, 3, 5], 
    [2, 6, 9], 
    [3, 6, 9]
]
print(median(matrix))
