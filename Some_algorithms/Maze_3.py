import math


def weighted_escape_length(maze, w, i=0, j=0):
    n = len(maze)
    m = len(maze[0])
    if i == n - 1 and j == m - 1:
        return 1

    if maze[i][j] == 1:
        maze[i][j] = 'one'
    else:
        maze[i][j] = 'zero'
    result = set()
    for a, b in [(i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1)]:
        if 0 <= a < n and 0 <= b < m and maze[a][b] == 0:
            count = weighted_escape_length(maze, w, a, b)
            count += 1
            result.add(count)
        elif 0 <= a < n and 0 <= b < m and maze[a][b] == 1:
            count = weighted_escape_length(maze, w, a, b)
            count += w
            result.add(count)
        else:
            result.add(math.inf)
    result = min(result)
    if maze[i][j] == 'one':
        maze[i][j] = 1
    else:
        maze[i][j] = 0
    return result


# Тесты 3
# test_a = [
#         [0, 0, 0],
#         [1, 1, 0],
#         [1, 1, 0]
#     ]
#
# test_b = [
#     [0, 0, 0],
#     [1, 1, 1],
#     [0, 0, 0]
# ]
#
# # should print 2
# print(weighted_escape_length(test_a, 0))
#
# # should print 5
# print(weighted_escape_length(test_b, 1))
#
# # should print 6
# print(weighted_escape_length(test_b, 2))
