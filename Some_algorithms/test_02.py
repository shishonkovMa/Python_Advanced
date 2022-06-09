n = int(input())
points = []
for i in range(n):
    x = [int(i) for i in input().split()]
    points.append(x)

summa = 0
for i in range(len(points)):
    if i == 0:
        summa += ((points[i][0]) ** 2 + (points[i][1]) ** 2) ** (1 / 2)
    else:
        summa += ((points[i][0] - points[i - 1][0]) ** 2 + (points[i][1]-points[i-1][1])**2)**(1/2)


itog_point = []
for i in range(len(points)):
    if i == 0:
        itog_point.append(points[i])
    elif i != 0 and points[i][1] > points[i-1][1]:
        itog_point.append(points[i])

for i in range(1, len(itog_point)):
    summa += ((itog_point[i][0]-itog_point[i-1][0])**2 + (itog_point[i][1]- itog_point[i-1][1])**2)**(1/2)

print(summa)

# 6
# 3 2
# 5 1
# 7 4
# 9 3
# 11 7
# 12 1
