# using Counter
from collections import Counter

def find_duplicates(s):
    di = Counter(s)
    for k, v in di.items():
        if v > 1:
            print(f'{k}: {v}')

# without using Counter
def find_duplicates1(s):
    di = {}
    for char in s:
        if char in di:
            di[char] += 1
        else:
            di[char] = 1
    
    for k, v in di.items():
        if v > 1:
            print(f'{k}: {v}')
