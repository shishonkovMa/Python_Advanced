dictionary = dict()

while True:
    input_line = input()
    if input_line == '':
        break

    for i in input_line.split():
        dictionary[i] = dictionary.setdefault(i, 0) + 1

new_dictionary = sorted(dictionary.items(), key=lambda d: (-d[1], d[0]))
final_output = [d[0] for d in new_dictionary]
for i in final_output:
    print(i)
# word_count_dict = dict()
#
# while True:
#     input_line = input()
#     if input_line == '':
#         break
#
#     for word in input_line.split():
#         word_count_dict[word] = word_count_dict.get(word, 0) + 1
#
# word_count_list = list(word_count_dict.items())
# print(word_count_list)
# word_count_list.sort(key=lambda x: (-x[1], x[0]))
# for word, cnt in word_count_list:
#     print(word)
