import math


def find_percentile(a, b, p):
    result = []
    i, j = 0, 0
    n = len(a)
    m = len(b)
    if n == 0 and m == 0:
        return -math.inf
    while i < n and j < m:
        if a[i] < b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    while i < n:
        result.append(a[i])
        i += 1
    while j < m:
        result.append(b[j])
        j += 1
    size = len(result)
    return result[int(math.ceil((size * p) / 100)) - 1]
