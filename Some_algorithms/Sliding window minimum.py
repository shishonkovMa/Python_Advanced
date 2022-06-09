import collections


def sliding_window_min(array, window):
    maximize = False
    result = []
    deque = collections.deque()
    for (i, val) in enumerate(array):
        val = array[i]
        while len(deque) > 0 and ((not maximize and val < deque[-1]) or (maximize and val > deque[-1])):
            deque.pop()
        deque.append(val)

        j = i + 1 - window
        if j >= 0:
            result.append(deque[0])
            if array[j] == deque[0]:
                deque.popleft()
    return result
