string = input().split()
s = int(string[0])
list_1 = []
count = 0

for i in range(int(string[1])):
    list_1.append(int(input()))

list_1.sort()

for i in list_1:
    if i < s:
        count += 1
        s -= i

print(count)
