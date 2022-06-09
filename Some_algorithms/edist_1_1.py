def edistance(a, b):
    n, m = len(a), len(b)
    if n > m:
        # убедимся что n <= m, чтобы использовать минимум памяти O(min(n, m))
        a, b = b, a
        n, m = m, n
    current_row = range(n + 1)  # 0 ряд - просто восходящая последовательность (одни вставки)
    for i in range(1, m + 1):
        previous_row, current_row = current_row, [i] + [0] * n
        for j in range(1, n + 1):
            add, delete, change = previous_row[j] + 1, current_row[j - 1] + 1, previous_row[j - 1]
            if a[j - 1] != b[i - 1]:
                change += 1
            current_row[j] = min(add, delete, change)
    return current_row[n]


# # Тесты
# # should print 1
# print(edistance("god", "good"))
#
# # should print 3
# print(edistance("good", "bad"))
#
# # should print 2
# print(edistance("a", "aaa"))




# Работающая вторая часть с ошибками в 5,7,14,15
# def weighted_edistance(s1, s2, wdel, wins, wsub):
#     m, n = len(s1), len(s2)
#     if m == 0:
#         return n*wins
#     if n == 0:
#         return m*wdel
#     mtx = [[0] * (n + 1) for _ in range(m + 1)]
#     for i in range(1, m + 1):
#         mtx[i][0] = i
#     for j in range(1, n + 1):
#         mtx[0][j] = j
#     for j in range(1, n + 1):
#         for i in range(1, m + 1):
#             if s1[i - 1] == s2[j - 1]:
#                 mtx[i][j] = mtx[i - 1][j - 1]
#             else:
#                 mtx[i][j] = min(mtx[i - 1][j]+wdel,  # удаление
#                                 mtx[i][j - 1]+wins,  # вставка
#                                 mtx[i - 1][j - 1]+wsub)  # замена
#     return mtx[-1][-1]
