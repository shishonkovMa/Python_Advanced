distances = [int(i) for i in input().split()]
rates = [int(i) for i in input().split()]

distances.sort()
rates.sort(reverse=True)

result = map()
summa = 0
for i in range(len(distances)):
    summa += distances[i]*rates[i]

print(summa)
