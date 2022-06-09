import json

input_file = input()

first = 0
second = 0
third = 0
fourth = 0
count = 0
with open(f'{input_file}') as f:
    for i in f:
        try:
            x = json.loads(i)
            try:
                x['status'] = int(x['status'])
                if x['status'] == 200:
                    first += 1
                elif x['status'] != 200:
                    second += 1
            except ValueError:
                if x['status'] != '':
                    third += 1
                else:
                    fourth += 1
                continue
            except KeyError:
                fourth += 1
                continue
            except TypeError:
                fourth += 1
                continue
        except json.JSONDecodeError:
            count += 1
            continue

print(first)
print(second)
print(third)
print(fourth)
print(count)
