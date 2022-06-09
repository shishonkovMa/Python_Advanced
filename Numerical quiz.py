import math as m

ls = []
dictionary = dict()

for i in range(int(input())):
    x = input()
    summa = 0
    for k in range(m.floor(len(x)/2)):
        summa += int(x[k])-int(x[-(k+1)])
    dictionary[int(x)] = summa

dict_list = list(dictionary.items())
new = sorted(dict_list, key=lambda d: (d[1], d[0]))
for k, v in new:
    print(k)
