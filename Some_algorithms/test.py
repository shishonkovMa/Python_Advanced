n = int(input())
rez = [int(i) for i in input().split()]
meetings = set()
dict_id = dict()
for i in range(n):
    dict_id[i] = [int(i) for i in input().split()][1:]
    if rez[i] or len(meetings.intersection(set(dict_id[i]))) != 0:
        meetings.update(set(dict_id[i]))

print(dict_id)
print(meetings)

covid = []
for k in range(n):
    print(meetings.intersection(set(dict_id[k])))
    if len(meetings.intersection(set(dict_id[k]))) != 0 or rez[k]:
        covid.append(1)
    else:
        covid.append(0)

print(*covid)

# Test 1
# 4
# 1 0 0 1
# 1 1
# 1 1
# 0
# 0


# Test 2
# 4
# 1 0 0 0
# 3 2 3 4
# 1 2
# 1 3
# 1 4
# -------
# 1 1 1 1


# Test 3
# 2
# 1 0
# 1 4
# 1 3
# -------
# 1 0


# Test 4
# 4
# 1 0 0 0
# 2 1 2
# 1 2 3
# 1 3
# 1 3
# -------
# 1 1 1 1


# Test 5
# 4
# 0 0 0 1
# 1 3
# 1 3
# 2 2 3
# 2 1 2
# -------
# 1 1 1 1