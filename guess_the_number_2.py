n = int(input())

august_choice_set = set(range(1, n+1))
answer_spis = []

while True:
    beatrice_guess = input()
    if beatrice_guess == 'HELP':
        break
    beatrice_guess = {int(x) for x in beatrice_guess.split()}
    if len(beatrice_guess & august_choice_set) > len(august_choice_set)/2:
        answer = 'YES'
        answer_spis.append(answer)
        august_choice_set &= beatrice_guess
    elif len(beatrice_guess & august_choice_set) <= len(august_choice_set)/2:
        answer = 'NO'
        answer_spis.append(answer)
        august_choice_set.difference_update(beatrice_guess)

for i in answer_spis:
    print(i, end='\n')
print(*sorted(august_choice_set), sep=' ')
