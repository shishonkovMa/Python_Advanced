import json

input_file = input()
with open(f'{input_file}') as f:
    values_ = json.load(f)

data = []
for key, value1 in values_.items():
    if len(value1) == 0:
        data.append(f"{key}")
    for key2, value2 in value1.items():
        if len(value2) == 0:
            data.append(f"{key}/{key2}")
        for key3, value3 in value2.items():
            if len(value3) == 0:
                data.append(f"{key}/{key2}/{key3}")
            for key4, value4 in value3.items():
                if len(value4) == 0:
                    data.append(f"{key}/{key2}/{key3}/{key4}")
                for key5, value5 in value4.items():
                    if len(value5) == 0:
                        data.append(f"{key}/{key2}/{key3}/{key4}/{key5}")
                    for key6, value6 in value5.items():
                        if len(value6) == 0:
                            data.append(f"{key}/{key2}/{key3}"
                                        f"/{key4}/{key5}/{key6}")
                        for key7, value7 in value6.items():
                            if len(value7) == 0:
                                data.append(f"{key}/{key2}/{key3}"
                                            f"/{key4}/{key5}/{key6}/{key7}")

for i in sorted(data):
    print(i)
