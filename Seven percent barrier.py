dictionary = dict()

while True:
    input_line = input()
    if input_line == 'PARTIES:':
        continue
    if input_line == 'VOTES:':
        break
    dictionary[input_line] = 0

while True:
    input_line = input()
    if input_line == '':
        break

    dictionary[input_line] += 1

for key, count in dictionary.items():
    if count/sum(dictionary.values()) * 100 > 7:
        print(key)
