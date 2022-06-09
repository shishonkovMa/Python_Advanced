import math


def fastest_escape_length(maze, i=0, j=0):
    n = len(maze)
    m = len(maze[0])
    if i == n - 1 and j == m - 1:
        return 1
    maze[i][j] = 1
    result = set()
    for a, b in [(i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1)]:
        if 0 <= a < n and 0 <= b < m and maze[a][b] == 0:
            count = fastest_escape_length(maze, a, b)
            count += 1
            result.add(count)
        else:
            result.add(math.inf)
    result = min(result)
    maze[i][j] = 0
    return result

# Тесты 1
# maze1 = [
#       [0, 0, 0, 0],
#       [1, 1, 1, 0],
#       [0, 0, 0, 0],
#       [0, 1, 1, 1],
#       [0, 0, 0, 0]
#     ]
#
# maze2 = [
#       [0, 0, 0],
#       [1, 0, 0],
#       [1, 1, 0]
#     ]
#
# print(fastest_escape_length(maze1))
# print(fastest_escape_length(maze2))
