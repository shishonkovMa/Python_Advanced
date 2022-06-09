def knapsack_full(W, V, C):
    n = len(W)
    tbl = [[0] * (C + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(C + 1):
            tbl[i][j] = tbl[i - 1][j]
            if j >= W[i - 1]:
                tbl[i][j] = max(
                    tbl[i][j],
                    tbl[i - 1][j - W[i - 1]] + V[i - 1]
                )

    knapsack = []
    i = n
    j = C
    while i > 0:
        if tbl[i][j] != tbl[i - 1][j]:
            j -= W[i - 1]
            knapsack.append(i - 1)
        i -= 1
    # Напечатать таблицу
    # print('\n'.join([str(l) for l in tbl]))
    return (tbl[-1][-1], knapsack)

# knapsack_full([1,4,5,4,3,3,2,1], [4,6,20,10,16,7,13,1], 12)