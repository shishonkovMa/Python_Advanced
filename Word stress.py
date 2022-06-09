n = int(input())
dictionary = dict()
set_of_words = set()

for i in range(n):
    word = input()
    set_of_words.add(word.lower())
    if word.lower() not in dictionary:
        dictionary.setdefault(word.lower(), []).append(word)
    else:
        dictionary[word.lower()].append(word)

peter_homework = str(input()).split()
count = 0

for i in peter_homework:
    if i.lower() in set_of_words:
        for k, l in dictionary.items():
            if i.lower() == k and i not in l:
                count += 1
    else:
        if not i.islower():
            count_liter = 0
            for liter in i:
                if liter.isupper():
                    count_liter += 1
            if count_liter > 1:
                count += 1
        else:
            count += 1
print(count)
