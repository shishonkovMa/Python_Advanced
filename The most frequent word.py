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

words_2 = []
for i in range(len(words_1)):
    if words_1[i] == max(words_1):
        words_2.append(spis[i])
print(*sorted(words_2)[0].split())
