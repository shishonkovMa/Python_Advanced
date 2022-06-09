n = int(input())

values_to_key = dict()
key_to_values = dict()

for _ in range(n):
    key, values = input().split(maxsplit=1)
    values_to_key[key] = values
    key_to_values[values] = key

n_queries = input()
if n_queries in values_to_key.keys():
    print(values_to_key[n_queries])
elif n_queries in values_to_key.values():
    print(key_to_values[n_queries])
