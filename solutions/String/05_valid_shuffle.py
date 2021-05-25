# pointer approach
def valid_shuffle(s1, s2, result):
    if len(s1) + len(s2) != len(result):
        return False
    else:
        i, j, k = 0, 0, 0
        while k < len(result):
            if i < len(s1) and s1[i] == result[k]:
                i += 1
            elif j < len(s2) and s2[j] == result[k]:
                j += 1
            else:
                return False
            k += 1
    return True
