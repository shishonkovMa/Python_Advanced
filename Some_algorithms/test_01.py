n = int(input())
rez = [int(i) for i in input().split()]
dict_id = dict()
sub_group = set()
for i in range(n):
    dict_id[i] = set(int(i) for i in input().split()[1:])
    if rez[i]:
        sub_group.update(dict_id[i])


def covid_m(id, cnt=0):
    global sub_group
    if cnt == n:
        return set()
    cnt += 1
    total = set()
    for i in dict_id[id]:
        for k in dict_id:
            if i in dict_id[k] and k != id and min(dict_id[k]) >= min(sub_group):
                total = dict_id[id].union(covid_m(k, cnt))
    return total


finish = set()
for i in range(n):
    if rez[i]:
        finish.update(covid_m(i))
        break

covid = []
for k in range(n):
    if len(dict_id[k]) != 0:
        if (len(finish.intersection(dict_id[k])) != 0 or rez[k]) and min(dict_id[k]) >= min(finish):
            covid.append(1)
        else:
            covid.append(0)
    else:
        if len(finish.intersection(dict_id[k])) != 0 or rez[k]:
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
# -------
# 1 1 0 1


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
# 0 0 1 0
# 1 3
# 1 5
# 2 1 2
# 2 2 3
# -------
# 1 0 1 1


# Test 6
# 3
# 0 1 1
# 2 2 3
# 2 3 4
# 2 4 6
# -------
# 0 1 1
