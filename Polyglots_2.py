lang = set()

n = int(input())
for i in reversed(range(n)):
    x = int(input())
    for k in range(x):
        lang.update(input().split())
print(len(lang))
print(*sorted(lang), sep='\n')
