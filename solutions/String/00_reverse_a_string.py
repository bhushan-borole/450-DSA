def reverse_string(self, s):
    # s : List[str]
    s.reverse()

# Two pointer approach
def reverse_string(self, s):
    # s : List[str]
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
