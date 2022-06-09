import re
result = []
while True:
    input_string = input()
    if input_string == '':
        break
    result.extend(re.findall(r"<i>(.*?)</i>", input_string))

[print(i) for i in result]
