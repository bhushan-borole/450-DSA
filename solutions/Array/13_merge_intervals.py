def merge(intervals):
    intervals.sort(key=lambda x: x[0])

    op = []
    for interval in intervals:
        if not op or op[-1][1] < interval[0]:
            op.append(interval)
        else:
            op[-1][1] = max(op[-1][1], interval[1])

    return op

intervals = [[1,3],[2,6],[8,10],[15,18]]
print(merge(intervals))
