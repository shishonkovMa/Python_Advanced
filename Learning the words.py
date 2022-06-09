ls = []

for i in range(int(input())):
    ls.append(input())

ls.sort(key=len)

for _ in range(len(ls)):
    for i in range(len(ls)):
        if len(ls[i]) == len(ls[i-1]) and ls[i][::-1] < ls[i-1][::-1]:
            a = ls[i-1]
            ls[i-1] = ls[i]
            ls[i] = a

[print(i) for i in ls]

# n_words = int(input())
# words = [input() for _ in range(n_words)]
# words.sort(key=lambda word: (len(word), word[::-1]))
# print(*words, sep='\n')