# def weighted_edistance(a, b, wdel, wins, wsub):
#     n, m = len(a), len(b)
#     d = [[0] * (m + 1) for _ in range(n + 1)]
#
#     for i in range(n):
#         d[i][0] = i
#     for j in range(m):
#         d[0][j] = j
#
#     for i in range(1, n):
#         for j in range(1, m):
#             if a[i-1] == b[j-1]:
#                 cost = 0
#             else:
#                 cost = wsub
#             d[i][j] = min(d[i - 1][j] + wdel,  # deletion
#                           d[i][j - 1] + wins,  # insertion
#                           d[i - 1][j - 1] + cost)  # substitution
#             if i > 1 and j > 1 and a[i] == b[j-1] and a[i-1] == b[j]:
#                 d[i][j] = min(d[i][j], d[i - 2][j - 2] + 1)  # transposition
#
#     return d[n][m]



# def weighted_edistance(A, B, wdel, wins, wsub):
#     n = len(A)
#     m = len(B)
#
#     D = [[0 for i in range(n+1)] for i in range(2)]
#
#     for i in range(1, n+1):
#         D[0][i] = i + wins
#
#     for i in range(1, m+1):
#         for j in range(0, n+1):
#             if j == 0:
#                 D[i % 2][j] = i
#             elif A[j-1] == B[i-1]:
#                 D[i % 2][j] = D[(i-1) % 2][j-1] + wsub
#             else:
#                 D[i % 2][j] = min(D[(i-1) % 2][j] + wdel,
#                                      D[i % 2][j-1] + wins,
#                                      D[(i-1) % 2][j-1])
#     return D[m % 2][n]


# print('\n'.join([str(l) for l in mtx]))
# # should print 7
# print(weighted_edistance("good", "bad", 1, 2, 5))
#
# # should print 5
# print(weighted_edistance("good", "bad", 1, 1, 3))
#
# # should print 6
# print(weighted_edistance("a", "aaa", 1, 3, 1))