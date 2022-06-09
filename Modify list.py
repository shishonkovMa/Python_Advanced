def modify_list(a):
    for i in reversed(range(len(a))):
        if a[i] % 2 == 0:
            a[i] = a[i] // 2
        else:
            del a[i]
