distances = list(map(int, input().split()))
rates = list(map(int, input().split()))
a = sorted(range(len(distances)), key=lambda x: distances[x])
b = sorted(range(len(rates)), key=lambda x: rates[x], reverse=True)
answer = dict(zip(a, b))
result = dict(sorted(answer.items(), key=lambda x: x[0]))
print(*result.values())
