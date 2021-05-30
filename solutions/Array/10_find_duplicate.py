from collections import Counter

def findDuplicate(nums):
    di = Counter(nums)
    for k, v in di.items():
        if v >= 2:
            return k

nums = [1, 2, 3, 4, 2]
print(findDuplicate(nums))
