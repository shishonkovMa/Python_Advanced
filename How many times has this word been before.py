import sys

spis = []

for input_line in sys.stdin:
    input_line = input_line.rstrip('\n')

    if input_line == '':
        break
    spis.extend(input_line)
    spis.append(' ')
spis = (''.join(spis)).split()

words = {}
words_1 = []

for x in spis:
    if x not in words:
        words[x] = 0
    else:
        words[x] += 1
    words_1.append(words[x])

print(*words_1)
