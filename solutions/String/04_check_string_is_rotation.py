def check_string_is_rotation(s1, s2):
    temp = s1 + s1
    if s2 in temp:
        return True
    return False
