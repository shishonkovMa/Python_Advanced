## если сломанный json (один словарь на разных строках).
## программа получает список всех словарей (в том числе и изначально поломанных)
## пример файла input_02.json

import json
import pandas as pd

input_file = str(input())
lists = []
with open(f'{input_file}') as f:
    data = ""
    for line in f.readlines():
        data += line.strip()
    data = data.replace("}{", "},\n{")

text = f"""
{data}
"""

data = json.loads('[' + text + ']')

df = pd.DataFrame(i for i in data)

# print(len(df['status'][df['status'].str.isalpha().notnull()]))

