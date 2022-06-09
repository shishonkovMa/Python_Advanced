def edistance(A, B):
    n = len(A)
    m = len(B)

    D = [[0 for i in range(n+1)] for i in range(2)]

    for i in range(1, n+1):
        D[0][i] = i

    for i in range(1, m+1):
        for j in range(0, n+1):
            if (j==0):
                D[i%2][j] = i
            elif A[j-1]==B[i-1]:
                D[i % 2][j] = D[(i-1)%2][j-1]
            else:
                D[i % 2][j] = (1+min(D[(i-1)%2][j],
                                     D[i%2][j-1],
                                     D[(i-1)%2][j-1]))
    return D[m%2][n]

# # Тесты
# # should print 1
# print(edistance("god", "good"))
#
# # should print 3
# print(edistance("good", "bad"))
#
# # should print 2
# print(edistance("a", "aaa"))