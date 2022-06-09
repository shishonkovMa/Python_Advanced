n = input().split()
number_of_days = int(n[0])
number_of_parties = int(n[1])
set_itog = set()
weekend = [6, 7]
saturday = 6

while True:
    saturday = saturday + 7
    sunday = saturday + 1
    if saturday > number_of_days:
        break
    weekend.extend([saturday, sunday])

for i in range(number_of_parties):
    x = input().split()
    for k in range(int(x[0]), number_of_days+1, int(x[1])):
        set_itog.add(k)

set_itog.difference_update(weekend)
print(len(set_itog))
