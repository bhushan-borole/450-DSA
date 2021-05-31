def search(nums, target):
    if target in nums:
        return nums.index(target)
    return -1

nums = [4, 5, 6, 7, 0, 1, 2]
print(search(nums, 0))
