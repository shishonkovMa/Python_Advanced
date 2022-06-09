def weighted_escapes(maze, w, i=0, j=0):
    n = len(maze)
    m = len(maze[0])
    if i == n - 1 and j == m - 1:
        return [[tuple([i, j])]]

    if maze[i][j] == 1:
        maze[i][j] = 'one'
    else:
        maze[i][j] = 'zero'

    result = []
    for a, b in [(i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1)]:
        if 0 <= a < n and 0 <= b < m and (maze[a][b] == 0 or maze[a][b] == 1):
            count = weighted_escapes(maze, w, a, b)
            # if maze[a][b] == 0:
            for p in count:
                p.insert(0, tuple([i, j]))
                result.append(p)

    if maze[i][j] == 'one':
        maze[i][j] = 1
    else:
        maze[i][j] = 0

    if len(result) != 0 and i == 0 and j == 0:
        pod_total = []
        for st in range(len(result)):
            cnt = 0
            for stl in range(len(result[st])):
                if maze[result[st][stl][0]][result[st][stl][1]] == 0:
                    cnt += 1
                elif maze[result[st][stl][0]][result[st][stl][1]] == 1:
                    cnt += w
            pod_total.append(cnt)
        total = []
        minim = pod_total[0]
        for k in range(len(pod_total)):
            if pod_total[k] < minim:
                total.clear()
                total.append(result[k])
                minim = pod_total[k]
            elif pod_total[k] == minim:
                total.append(result[k])
        return total
    else:
        return result


# # # Тесты 4
# test_b = [
#     [0, 0, 0],
#     [1, 1, 1],
#     [0, 0, 0]
# ]
# # should print [[(0, 0), (1, 0), (1, 1), (1, 2), (2, 2)]]
# print(weighted_escapes(test_b, 0))
# # # should print [[(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)], [(0, 0), (0, 1), (1, 1), (2, 1), (2, 2)], [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2)]]
# # # the order of the paths within the list might be different
# print(weighted_escapes(test_b, 2))