lang = set()
lang_1 = set()

n = int(input())
for i in range(n):
    x = int(input())
    for k in range(x):
        s = input()
        lang.add(s)
    if i == 0:
        lang_1.update(lang)
    else:
        lang_1.intersection_update(lang)
    lang.clear()

print(len(lang_1))
print(*sorted(lang_1), sep='\n')
