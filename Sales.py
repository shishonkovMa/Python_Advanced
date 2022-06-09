dictionary = dict()

while True:
    input_line = input()
    if input_line == '':
        break

    k1, k2, v = input_line.split(maxsplit=2)
    dictionary.setdefault(k1, dict())
    dictionary[k1][k2] = dictionary[k1].setdefault(k2, 0) + int(v)

for i in sorted(dictionary):
    print(i, ':', sep='')
    sortirov = sorted(dictionary[i])
    for k in sortirov:
        print(k, dictionary[i][k])
