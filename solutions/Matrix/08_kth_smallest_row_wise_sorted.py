def kthSmallest(matrix, k):
    flatten = [elem for row in matrix for elem in row]
    flatten.sort()
    return flatten[k-1]

matrix = [[1,5,9],[10,11,13],[12,13,15]]
k = 8
print(kthSmallest(matrix, k))
