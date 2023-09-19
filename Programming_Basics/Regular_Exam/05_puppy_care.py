total_food = int(input())
food_in_grams = total_food * 1000
total_eaten_food = 0

input_line = input()
while input_line != 'Adopted':
    food_per_day = int(input_line)
    total_eaten_food += food_per_day

    input_line = input()

diff = abs(total_eaten_food - food_in_grams)

if total_eaten_food <= food_in_grams:
    print(f'Food is enough! Leftovers: {diff} grams.')
else:
    print(f'Food is not enough. You need {diff} grams more.')