def lines(a):
    start = len(a)
    total_a = a.copy()
    dlina_new = 0
    while len(a) > dlina_new:
        line = 0
        color = 0
        a = total_a.copy()
        total_a = a.copy()
        for i in range(len(a)):
            if i == 0:
                color = a[i]
                line = 1
            elif a[i] == color:
                line += 1
            elif a[i] != color:
                if line >= 3:
                    for k in range(line):
                        total_a.pop(i - 1 - k)
                color = a[i]
                line = 1
        if line >= 3:
            for k in range(line):
                total_a.pop(i - 1 - k)
        dlina_new = len(total_a)
    finish = len(total_a)
    return start - finish


if __name__ == "__main__":
    test_a = [2, 2, 1, 1, 1, 2, 1]
    # should print 6
    print(lines(test_a))

    test_a = [0, 0, 0, 0, 0]
    # should print 5
    print(lines(test_a))

    test_a = [2, 3, 1, 4]
    # should print 0
    print(lines(test_a))