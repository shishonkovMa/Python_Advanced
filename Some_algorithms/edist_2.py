def weighted_edistance(s1, s2, wdel, wins, wsub):

    m, n = len(s1), len(s2)

    if m == 0:
        return n*wins
    if n == 0:
        return m*wdel
    mtx = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:
                mtx[i][j] = j
            elif j == 0:
                mtx[i][j] = i
            elif s1[i - 1] == s2[j - 1]:
                mtx[i][j] = mtx[i - 1][j - 1]
            elif len(s1[:i-1]) == len(s1) and len(s2[:j - 1]) != len(s2) and j > i:
                mtx[i][j] = mtx[i][j - 1] + wins * (n-m)
            else:
                mtx[i][j] = min(mtx[i - 1][j]+wdel,  # удаление
                                mtx[i][j - 1]+wins,  # вставка
                                mtx[i - 1][j - 1]+wsub)  # замена
    print('\n'.join([str(l) for l in mtx]))
    return mtx[-1][-1]


# should print 4
print(weighted_edistance("goodest", "gooder", 1, 2, 5))

# should print 5
print(weighted_edistance("good", "bad", 1, 1, 3))
#
# should print 3
print(weighted_edistance("a", "af", 1, 3, 1))