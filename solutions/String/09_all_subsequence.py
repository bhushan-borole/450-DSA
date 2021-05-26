op = []

def helper(res, i, j, s):
    if i == j:
        op.append(res)
    else:
        helper(res, i+1, j, s)
        helper(res + s[i], i+1, j, s)

def all_subsequence(s):
    helper('', 0, len(s), s)
    return op
