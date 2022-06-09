import json

s = [input() for i in range(int(input()))]
fail = str(input())

unique_1 = set()
unique_2 = []
for i in s:
    unique_1.add(i[0])
    unique_2.append(i[:2])
unique_2 = set(unique_2)

d = dict()

for i in unique_1:
    d.setdefault(i, {})
    for k in unique_2:
        for si in s:
            if i in k[0] and k == si[:2]:
                d[i].setdefault(k, []).append(si)
                d[i][k].sort()

with open(fail, 'w') as fw:
    json.dump(d, fw)


# import json
# from collections import defaultdict
#
#
# n_words = int(input())
# words = [input() for _ in range(n_words)]
# output_filename = input()
#
# search_index = defaultdict(dict)
# for word in words:
#     search_index[word[0]].setdefault(word[:2], []).append(word)
#
# search_index = {
#     key: {a: sorted(b) for a, b in value.items()}
#     for key, value in search_index.items()
# }
#
# with open(output_filename, 'w') as f:
#     json.dump(search_index, f)