import math

def countSquares(n):
    return math.ceil(math.sqrt(n)) - 1

n = 9
print(countSquares(n))
