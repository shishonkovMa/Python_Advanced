dictionary = dict()
list_city = []

n = int(input())
for _ in range(n):
    x = input().split()
    dictionary[x[0]] = x[1:]

m = int(input())

for _ in range(m):
    list_city.append(input())

for i in list_city:
    for k in dictionary.keys():
        if i in dictionary[k]:
            print(k)
