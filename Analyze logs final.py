# import json
# import pandas as pd
#
# input_file = str(input())
# lists = []
# with open(f'{input_file}') as f:
#     data = list(f)
#
# count = 0
# final = []
# for i in data:
#     try:
#         xn = json.loads(i.replace("'", '"'))
#         final.append(xn)
#     except ValueError:
#         count += 1
#         continue
#
# df = pd.DataFrame(i for i in final)
# print(df.iloc[18:30])
# first = len(df.query('status == 200 or status == "200"'))
# second = len(df.query('status in (305, 418, 204, 404, 502, '
#                       '"305", "418", "204", "404", "502")'))
# a = len(df.query('status == ""'))
# b = len(df[df['status'].isna()])
# fourth = a+b
# third = len(df) - first - second - fourth
#
# print(first)
# print(second)
# print(third)
# print(fourth)
# print(count)


# input_02.json
# C:/Users/bosss/py_projects/2.3 week/input_02.json


# df = pd.DataFrame(i for i in lists)
# first = len(df[df['status'] == 200])
# second = len(df[(pd.to_numeric(df.status, errors='coerce')
#                  .notnull()) & (df.status != 200)])
# a = len(df.query('status == ""'))
# b = len(df[df['status'].isna()])
# fourth = a+b
# third = len(df) - first - second - fourth