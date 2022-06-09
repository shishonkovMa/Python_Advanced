n = int(input())

august_choice_set = set(range(1, n+1))
beatrice_guess = set()
guess_yes = set()
guess_no = set()

while True:
    beatrice_guess = input()
    if beatrice_guess == 'HELP':
        break
    beatrice_guess = {int(x) for x in beatrice_guess.split()}
    answer = input()
    if answer == 'YES':
        august_choice_set.intersection_update(beatrice_guess)
    else:
        august_choice_set.difference_update(beatrice_guess)

print(*sorted(august_choice_set), sep=' ')
