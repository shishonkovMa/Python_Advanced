dictionary = dict()
output = []

while True:
    input_line = input()
    if input_line == '':
        break

    for word in input_line.split():
        output.append(dictionary.get(word, -1))
        dictionary[word] = len(output) - 1

print(*output, sep=' ')
