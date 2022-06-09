import math as m

dictionary = dict()
output = []

while True:
    input_line = input()
    if input_line == '':
        break

    x = input_line.split()

    if 'DEPOSIT' in input_line:
        if x[1] not in dictionary:
            dictionary[x[1]] = int(x[2])
        else:
            dictionary[x[1]] = dictionary[x[1]] + int(x[2])
    elif 'WITHDRAW' in input_line:
        if x[1] not in dictionary:
            dictionary[x[1]] = - int(x[2])
        else:
            dictionary[x[1]] = dictionary[x[1]] - int(x[2])
    elif 'BALANCE' in input_line:
        output.append(dictionary.get(x[1], 'ERROR'))
    elif 'TRANSFER' in input_line:
        if x[1] not in dictionary and x[2] not in dictionary:
            dictionary[x[1]] = - int(x[3])
            dictionary[x[2]] = int(x[3])
        elif x[1] not in dictionary and x[2] in dictionary:
            dictionary[x[1]] = - int(x[3])
            dictionary[x[2]] = dictionary[x[2]] + int(x[3])
        elif x[1] in dictionary and x[2] not in dictionary:
            dictionary[x[1]] = dictionary[x[1]] - int(x[3])
            dictionary[x[2]] = int(x[3])
        elif x[1] in dictionary and x[2] in dictionary:
            dictionary[x[2]] = dictionary[x[2]] + int(x[3])
            dictionary[x[1]] = dictionary[x[1]] - int(x[3])
    elif 'INCOME' in input_line:
        for i in dictionary:
            if dictionary[i] > 0:
                dictionary[i] = m.floor(dictionary[i] * (1 + int(x[1])/100))

for i in output:
    print(i)
