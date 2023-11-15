food, hay, cover, weight = float(input()), float(input()), float(input()), float(input())
food_gr = food * 1000
hay_gr = hay * 1000
cover_gr = cover * 1000
weight_gr = weight * 1000
flag = False
for day in range(1, 31):
    food_gr -= 300
    if day % 2 == 0:
        hay_gr -= food_gr * 0.05
    if day % 3 == 0:
        cover_gr -= weight_gr // 3
    if food_gr <= 0 or hay_gr <= 0 or cover_gr <= 0:
        flag = True
        break
if flag:
    print('Merry must go to the pet store!')
else:
    print(f'Everything is fine! Puppy is happy! Food: {(food_gr / 1000):.2f}, Hay: {(hay_gr / 1000):.2f}, Cover: {(cover_gr / 1000):.2f}.')
