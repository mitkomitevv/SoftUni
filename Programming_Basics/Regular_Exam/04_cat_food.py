count_cats = int(input())
group_1, group_2, group_3 = 0, 0, 0
total_food = 0

for _ in range(count_cats):
    food_in_grams = float(input())
    total_food += food_in_grams

    if 100 <= food_in_grams < 200:
        group_1 += 1
    elif 200 <= food_in_grams < 300:
        group_2 += 1
    elif 300 <= food_in_grams < 400:
        group_3 += 1

total_food_price = (total_food / 1000) * 12.45

print(f'Group 1: {group_1} cats.')
print(f'Group 2: {group_2} cats.')
print(f'Group 3: {group_3} cats.')
print(f'Price for food per day: {total_food_price:.2f} lv.')
