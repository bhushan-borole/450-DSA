def check_elem(elem, mat):
    for row in mat:
        if elem not in row:
            return False
    return True

def common_elements(mat):
    flatten = list(set([elem for row in mat for elem in row]))
    op = []
    for elem in flatten:
        if check_elem(elem, mat):
            op.append(elem)
    return op
