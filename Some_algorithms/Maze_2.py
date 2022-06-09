def fastest_escapes(maze, i=0, j=0):
    n = len(maze)
    m = len(maze[0])
    if i == n - 1 and j == m - 1:
        return [[tuple([i, j])]]
    maze[i][j] = 1
    result = []
    for a, b in [(i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1)]:
        if 0 <= a < n and 0 <= b < m and maze[a][b] == 0:
            cell = fastest_escapes(maze, a, b)
            for p in cell:
                p.insert(0, tuple([i, j]))
                result.append(p)
    if len(result) != 0:
        result_total = []
        minim = len(result[0])
        for k in range(len(result)):
            if len(result[k]) < minim:
                result_total.clear()
                result_total.append(result[k])
                minim = len(result[k])
            elif len(result[k]) == minim:
                result_total.append(result[k])
        maze[i][j] = 0
        return result_total
    else:
        maze[i][j] = 0
        return []

# Тесты 2
# test_a = [
#     [0, 0, 0],
#     [1, 1, 0],
#     [1, 1, 0]
# ]
#
# test_b = [
#     [0, 0, 0],
#     [1, 1, 1],
#     [0, 0, 0]
# ]
#
# maze1 = [
#       [0, 0, 0, 0],
#       [0, 1, 1, 1],
#       [0, 0, 0, 0],
#       [0, 1, 1, 0],
#       [0, 0, 0, 0]
#     ]
#
# print(fastest_escapes(maze1))
# # should print [[(0, 0), (0, 1), (0, 2), (1, 2), (2, 2)]]
# print(fastest_escapes(test_a))
#
# # should print []
# print(fastest_escapes(test_b))
#
# # should print [5, 5, 5, 5, 5, 5]
# print(list(map(len, fastest_escapes([[0 for _ in range(3)] for _ in range(3)]))))