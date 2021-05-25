import re


def count_and_say(n):
    s = '1'
    for _ in range(n - 1):
        s = re.sub(r'(.)\1*', lambda x: str(len(x.group(0))) + x.group(1), s)
    return s
