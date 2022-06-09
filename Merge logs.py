input_file, output_file = input().split(), str(input())

full_input = []
for i in range(len(input_file)):
    with open(f'{input_file[i]}') as f:
        input = list(f)
        full_input.extend(input)

final = []
for i in full_input:
    xn = eval(i)
    final.append(xn)

final_fin = sorted(final, key=lambda x: (x['date'], x['consumer_id']))

with open(output_file, 'w') as fw:
    for i in final_fin:
        fw.write(f'{i["date"]}\t{i["message"]}')
        fw.write('\n')
fw.close()
