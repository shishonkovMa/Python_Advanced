n = int(input())
x_new = list(set(int(i) for i in input().split() if int(i) >= n))
x_new.sort()

spis = []
dlina = n


def size(x):
    global dlina
    for i in x:
        if i == n or i-3 >= dlina or len(spis) == 0:
            spis.append(i)
            dlina = i
            x.remove(i)
            size(x)
    return spis


final_spis = size(x_new)
print(len(final_spis))
